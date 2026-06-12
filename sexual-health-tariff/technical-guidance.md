# Technical Guidance

> This page provides technical details for organisations submitting data to the Tariff Grouper.

## Overview

The Sexual Health Tariff Grouper accepts activity data from provider organisations and applies tariff configurations to calculate payment values. This guide covers the technical requirements for preparing and submitting data, including file formats, field specifications, validation rules, and how errors are handled during the upload process.

This guidance is intended for data analysts, IT teams, and information managers at provider organisations responsible for preparing and uploading activity data.

## File Formats

Data must be submitted in **CSV (Comma-Separated Values)** format. Files should conform to the following specifications:

| Property | Requirement |
|----------|-------------|
| Encoding | UTF-8 |
| Line endings | CRLF (`\r\n`) or LF (`\n`) |
| Delimiter | Comma (`,`) |
| Text qualifier | Double quotes (`"`) where fields contain commas or line breaks |
| Header row | Required — first row must contain column names exactly as specified |
| File extension | `.csv` |

### Formatting Notes

- Do not include byte order marks (BOM) in the file
- Ensure there are no trailing commas or empty rows at the end of the file
- Column order must match the specification — the system uses positional matching against the header row

## Field Specifications

The following fields are expected in each submission file. All fields are case-insensitive in the header row but must be present.

| Field Name | Format | Required | Description |
|------------|--------|----------|-------------|
| Patient ID | Alphanumeric (max 20 chars) | Yes | Pseudonymised patient identifier — must not contain identifiable information |
| Attendance Date | DD/MM/YYYY | Yes | Date of the patient attendance or activity |
| Clinic ID | Alphanumeric (max 10 chars) | Yes | ODS code or local clinic identifier |
| Provider Code | Alphanumeric (max 10 chars) | Yes | ODS code of the submitting provider organisation |
| SHHAPT Code | Alphanumeric | No | Sexual Health and HIV Activity Property Type code |
| Episode Activity | Alphanumeric | No | Episode activity code for the attendance |
| SRH Care Activity | Alphanumeric | No | Sexual and reproductive health care activity code |
| Contraceptive Code | Alphanumeric | No | Contraceptive method or intervention code |

### Field Details

**Patient ID**
A pseudonymised identifier that allows the grouper to link attendances for the same patient across a submission period. This must not be an NHS number or any directly identifiable information. Providers should use their local pseudonymisation process to generate consistent identifiers.

**Attendance Date**
Must be in DD/MM/YYYY format (e.g., `15/03/2024`). The date must fall within the active configuration period for the relevant tariff arrangement.

**Clinic ID**
The ODS code for the clinic where the activity took place, or a local identifier if no ODS code is available. This is used to map activity to specific service locations within the tariff configuration.

**Provider Code**
The ODS code of the provider organisation submitting the data. This must match the provider code registered against the active subscription.

**Activity Codes (SHHAPT, Episode Activity, SRH Care Activity, Contraceptive Code)**
These codes describe the clinical activity that took place during the attendance. At least one activity code should be present per row. The grouper uses these codes to classify the attendance into the appropriate tariff band. Recognised code values are defined within the active tariff configuration.

## Validation Rules

Data is validated automatically on upload. The system checks each row against the following rules before processing:

### Required Field Validation

- **Patient ID** must not be empty
- **Attendance Date** must not be empty
- **Clinic ID** must not be empty
- **Provider Code** must not be empty

### Format Validation

- **Attendance Date** must be a valid calendar date in DD/MM/YYYY format
- **Attendance Date** must fall within the active configuration period
- **Patient ID** must not exceed 20 characters
- **Patient ID** must contain only alphanumeric characters (letters and numbers)
- **Clinic ID** and **Provider Code** must not exceed 10 characters

### Code Validation

- **Activity codes** (SHHAPT, Episode Activity, SRH Care Activity, Contraceptive Code) must be recognised values defined in the active tariff configuration
- Unrecognised activity codes generate a warning but may not prevent processing, depending on the configuration

### Duplicate Detection

- Rows with identical Patient ID, Attendance Date, Clinic ID, and activity codes are flagged as potential duplicates
- Duplicate records are reported in the validation output for review

## Error Handling

When validation fails, the system provides detailed feedback to help you identify and correct issues.

### Error Responses

Errors are returned immediately after upload with the following information:

- **Row number** — the specific row in the CSV where the error was found
- **Field name** — the column that failed validation
- **Error type** — a code indicating the nature of the failure (e.g., `MISSING_REQUIRED`, `INVALID_DATE`, `UNRECOGNISED_CODE`)
- **Description** — a human-readable explanation of what went wrong

### Rejection Behaviour

- If **any row** contains a validation error, the **entire submission is rejected**
- No partial processing takes place — you must correct all errors and re-upload the complete file
- The error report is available to download immediately after submission

### Warnings

Some issues are flagged as warnings rather than errors:

- Unrecognised activity codes that may be valid but are not in the current configuration
- Potential duplicate rows that may represent legitimate repeat attendances
- Dates near the boundary of the configuration period

Warnings do **not** prevent processing. They are included in the validation output for your review and do not require action unless you identify a genuine data issue.

## Integration Requirements

### System Access

The Tariff Grouper is accessed via a web-based portal. There is no API integration currently available.

| Requirement | Detail |
|-------------|--------|
| Access method | Web browser via HTTPS |
| URL | [https://secure.pathwayanalytics.com](https://secure.pathwayanalytics.com/common/) |
| Authentication | Username and password (provided on subscription setup) |
| Browser support | Any modern browser with JavaScript enabled (Chrome, Firefox, Edge, Safari) |
| Connectivity | Standard HTTPS (port 443) — no VPN or special network configuration required |

### File Size and Submission Limits

| Constraint | Limit |
|------------|-------|
| Maximum file size | 10 MB per upload |
| Maximum rows | 100,000 rows per file |
| Submission frequency | No hard limit — submit as often as needed within the configuration period |

### Submission Workflow

1. Log in to the Tariff Grouper at [https://secure.pathwayanalytics.com](https://secure.pathwayanalytics.com/common/)
2. Navigate to the data upload area
3. Select the relevant tariff configuration
4. Upload your prepared CSV file
5. Review the validation results
6. If errors are present, download the error report, correct the data, and re-upload
7. Once validation passes, confirm the submission for processing

### Network and Security

- All data is transmitted over HTTPS with TLS encryption
- No data is stored locally in the browser after the session ends
- Sessions expire after a period of inactivity — you will need to log in again

## Additional Resources

For more information on related topics, refer to:

- [Provider Onboarding](/sexual-health-tariff/provider-onboarding) — subscription setup and getting started
- [Grouper Process](/sexual-health-tariff/grouper-process) — end-to-end tariff calculation workflow
- [Subscriptions & Pricing](/sexual-health-tariff/subscriptions) — subscription types and access levels
