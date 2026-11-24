#!/usr/bin/env bash
# Serve the docs site on the bare domain and www without redirecting.
#
#   pathwayanalytics.com      -> CloudFront -> docs.pathwayanalytics.com (GitHub Pages)
#   www.pathwayanalytics.com  -> same distribution
#   docs.pathwayanalytics.com -> GitHub Pages directly (not touched by this script)
#
# GitHub Pages allows one custom domain per site, so CloudFront fetches the page from
# docs. and presents it under the apex and www names. CloudFront sends the origin's
# Host header (docs.), which is what GitHub Pages routes on.
#
# Idempotent: reuses an existing certificate and distribution, and UPSERTs DNS.
# Usage: AWS_PROFILE=<profile that owns the zone> ./infra/apex-proxy.sh
# Requires: aws CLI v2, python3. Teardown: see the end of this file.
set -euo pipefail

ZONE_ID="Z3EVR19UG114IS"
APEX="pathwayanalytics.com"
WWW="www.${APEX}"
ORIGIN="docs.${APEX}"
CF_ALIAS_ZONE="Z2FDTNDATAQYW2"            # fixed hosted zone ID for all CloudFront aliases
CACHING_OPTIMIZED="658327ea-f89d-4fab-a63d-7e88639e58f6"
CALLER_REF="pwa-apex-docs"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

echo "Account: $(aws sts get-caller-identity --query Account --output text)"

# 1. ACM certificate (must be us-east-1 for CloudFront), apex + www
CERT_ARN=$(aws acm list-certificates --region us-east-1 --output json | python3 -c '
import json,sys
for c in json.load(sys.stdin)["CertificateSummaryList"]:
    if c["DomainName"]=="'"$APEX"'" and "'"$WWW"'" in c.get("SubjectAlternativeNameSummaries",[]) and c["Status"] in ("ISSUED","PENDING_VALIDATION"):
        print(c["CertificateArn"]); break')
if [ -z "$CERT_ARN" ]; then
  CERT_ARN=$(aws acm request-certificate --region us-east-1 --domain-name "$APEX" \
    --subject-alternative-names "$WWW" --validation-method DNS \
    --query CertificateArn --output text)
  sleep 10
fi
echo "Certificate: $CERT_ARN"

# 2. DNS validation records, then wait for issuance
aws acm describe-certificate --region us-east-1 --certificate-arn "$CERT_ARN" \
  --query "Certificate.DomainValidationOptions[].ResourceRecord" --output json | python3 -c '
import json,sys
recs=[r for r in json.load(sys.stdin) if r]
print(json.dumps({"Changes":[{"Action":"UPSERT","ResourceRecordSet":{"Name":r["Name"],"Type":"CNAME","TTL":300,"ResourceRecords":[{"Value":r["Value"]}]}} for r in recs]}))' > "$WORK/validation.json"
aws route53 change-resource-record-sets --hosted-zone-id "$ZONE_ID" --change-batch "file://$WORK/validation.json" >/dev/null
aws acm wait certificate-validated --region us-east-1 --certificate-arn "$CERT_ARN"
echo "Certificate issued"

# 3. CloudFront distribution (create if no distribution already carries the apex alias)
DIST_ID=$(aws cloudfront list-distributions --output json | python3 -c '
import json,sys
d=json.load(sys.stdin).get("DistributionList",{}).get("Items") or []
for x in d:
    if "'"$APEX"'" in (x.get("Aliases",{}).get("Items") or []):
        print(x["Id"]); break')
if [ -z "$DIST_ID" ]; then
  cat > "$WORK/dist.json" <<EOF
{
 "CallerReference": "${CALLER_REF}",
 "Comment": "Apex and www proxy to ${ORIGIN} (GitHub Pages)",
 "Aliases": {"Quantity": 2, "Items": ["${APEX}", "${WWW}"]},
 "Origins": {"Quantity": 1, "Items": [{"Id": "docs-github-pages", "DomainName": "${ORIGIN}",
   "CustomOriginConfig": {"HTTPPort": 80, "HTTPSPort": 443, "OriginProtocolPolicy": "https-only",
     "OriginSslProtocols": {"Quantity": 1, "Items": ["TLSv1.2"]}}}]},
 "DefaultCacheBehavior": {"TargetOriginId": "docs-github-pages", "ViewerProtocolPolicy": "redirect-to-https",
   "AllowedMethods": {"Quantity": 2, "Items": ["GET", "HEAD"]}, "Compress": true,
   "CachePolicyId": "${CACHING_OPTIMIZED}"},
 "Enabled": true, "HttpVersion": "http2and3", "IsIPV6Enabled": true, "PriceClass": "PriceClass_100",
 "ViewerCertificate": {"ACMCertificateArn": "${CERT_ARN}", "SSLSupportMethod": "sni-only",
   "MinimumProtocolVersion": "TLSv1.2_2021"}
}
EOF
  DIST_ID=$(aws cloudfront create-distribution --distribution-config "file://$WORK/dist.json" \
    --query Distribution.Id --output text)
fi
DIST_DOMAIN=$(aws cloudfront get-distribution --id "$DIST_ID" --query Distribution.DomainName --output text)
echo "Distribution: $DIST_ID ($DIST_DOMAIN)"
aws cloudfront wait distribution-deployed --id "$DIST_ID"

# 4. Alias A and AAAA records for apex and www (replaces any existing A record on those names)
python3 - "$DIST_DOMAIN" "$CF_ALIAS_ZONE" "$APEX" "$WWW" > "$WORK/dns.json" <<'EOF'
import json,sys
dom,zone,*names=sys.argv[1:]
print(json.dumps({"Changes":[{"Action":"UPSERT","ResourceRecordSet":{"Name":n+".","Type":t,
  "AliasTarget":{"HostedZoneId":zone,"DNSName":dom+".","EvaluateTargetHealth":False}}}
  for n in names for t in ("A","AAAA")]}))
EOF
aws route53 change-resource-record-sets --hosted-zone-id "$ZONE_ID" --change-batch "file://$WORK/dns.json" >/dev/null
echo "DNS updated. Verify:"
for h in "$APEX" "$WWW" "$ORIGIN"; do
  printf '%s -> ' "$h"; curl -s -o /dev/null -w '%{http_code} %{url_effective}\n' "https://$h/"
done

# Teardown (manual):
#   1. Delete the A/AAAA alias records for the apex and www in zone $ZONE_ID
#      (restore www to an A record if it should point elsewhere).
#   2. aws cloudfront update-distribution to Enabled=false, wait, then delete-distribution.
#   3. Optionally delete the certificate and its www validation CNAME.
