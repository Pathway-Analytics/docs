# File Validation

Every file you upload is validated before it can be used in a submission. Validation checks each record against the field definitions for your tariff configuration and reports any problems so you can fix them. A submission can only run once all its files are clear of errors.

## Overview

Validation runs automatically as soon as a file is uploaded. There is nothing to trigger manually — the Grouper reads the file, parses it, and checks every cell. You see the outcome on the file's validation summary: how many records were accepted, and any errors or warnings to resolve.

## File upload

When you upload a file, the Grouper:

1. Reads the file from secure storage and parses it (CSV or Excel).
2. Loads the field definitions and valid codes for your configuration.
3. Validates every data row, in batches for large files.
4. Stores the parsed, validated rows ready for the submission process.

The header row is used to map each column to a field; data rows are validated against those fields.

## Validation checks

Each cell is checked against its field definition. There are three kinds of error:

- **Mandatory** — a required field is empty. *"&lt;field&gt; is mandatory and cannot be empty."*
- **Format** — the value does not match the pattern the field requires (for example a date or a coded value). *"Value &lt;x&gt; does not match required format."*
- **Valid option** — the field draws from a controlled list of codes and the value is not one of them. *"&lt;x&gt; is not a valid option for this field."*

See [Preparing Your Data](/sexual-health-tariff/dataset) for how to get these right before you upload.

## After the validation check

### Notifications

When validation completes, the Grouper records the outcome against the file and the submission. Errors are listed in the submission's **validation errors** tab, grouped so you can work through them.

### Fixing validation errors

To clear errors, correct them at source and re-upload the file, or edit the affected records where the application allows. Because validation re-runs on every upload, a corrected file is re-checked immediately. Work through the validation errors tab until it is empty.

### Cleared to run the submission process

Once every file in the submission is clear of validation errors — and the submission's clinics and tariff configuration are valid — the submission is ready to process. The [Submission Process](/sexual-health-tariff/grouper-submission-process) page explains what happens next.

{{segment:copyright:link-modal}}
