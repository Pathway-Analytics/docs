# Submission Process

The submission process is the tariff calculation the Grouper runs over a provider's monthly activity to arrive at the charges. It relies on the month's data being valid, the clinics being properly identified, and a tariff configuration being available for that month. Once a submission completes as **Submitted**, its charges become visible to both the provider and the commissioners.

## What a submission is

A submission is a collection of the activity files a provider has uploaded for a single month, together with all the calculations and charges derived from that data. Each submission belongs to one provider and one month.

## Draft and Submitted

There are two ways to run the process, and the steps are identical — only the outcome differs:

- **Draft** — calculates tariffs without locking the submission. Charging data is **not** released to commissioners. Use it to check your figures.
- **Submitted** — locks the submission, prevents further changes, and **releases** the charging data to commissioners.

## Time constraints

Each tariff configuration has a **Submit Within** window — 21 days by default. The submission must be submitted within that many days of the prior month's end.

## Before a submission can run

A submission must be in a fit state to process:

- **Files clear of validation errors** — any file with validation errors must be corrected first, via the submission's validation errors tab (see [File Validation](/sexual-health-tariff/file-validation-process)).
- **Valid clinics** — any new clinic used in the uploaded files must have its address and host commissioner identified, in the submission's clinics tab.
- **Valid tariff configuration** — a configuration must be available for the month. If none is, contact your host commissioner or [enquiries@pathwayanalytics.com](mailto:enquiries@pathwayanalytics.com).

## Locking and resetting

- A submission **in processing** is locked; you cannot upload files while it runs.
- A **Draft** submission can be adjusted — upload new files or delete uploaded ones — but doing so clears its charging data.
- A **Submitted** submission can no longer be adjusted or re-processed.

## What the process does

Once started, the Grouper works through the submission in sequence:

1. **Collect the tariff configuration** — load the configuration that applies to the submission's month, with its currencies, rates and rules.
2. **Apply currencies** — match each episode's activity against the currency triggers to determine which currencies are raised.
3. **Apply invalid currency combinations** — suppress currencies that should not co-occur, per the configuration's invalid-combination rules.
4. **Apply cross-charging** — determine, for each currency, which commissioner is charged, following the currency's cross-charging arrangement.
5. **Identify the responsible commissioner** — resolve the paying commissioner from the patient's residence, or fall back to the clinic's host commissioner where the rules require.
6. **Calculate tariff rates and apply MFF / geo-weighting** — price each currency (primary rate for the most expensive currency in an episode, additional rate for the rest) and apply the provider's market forces factor or the clinic's geo-weighting.

See [Grouper Rules](/sexual-health-tariff/grouper-rules) and [Tariff Configurations](/sexual-health-tariff/tariff-configurations) for how currencies, episodes and cross-charging are defined.

## After a submission

- **Notifications** — the Grouper records completion and notifies as configured.
- **KPI calculation** — key performance indicators are calculated from the submitted data for reporting.

{{segment:copyright:link-modal}}
