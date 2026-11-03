# Preparing Your Data

Before the Grouper can calculate charges, your activity data has to be in the right shape. This page explains what a data file needs to contain, the formats accepted, and the checks your file is put through on upload. Get this right and your submission clears validation first time.

## What you submit

A submission is a collection of activity files for **one provider** and **one month**, together with the charges the Grouper calculates from them. You upload activity data as a file; the Grouper parses it, validates every row, and — once the file is clear — makes it available to run a submission.

## File formats

The Grouper accepts **CSV and Excel** files. The first row must be the header row naming each field; every row below it is one activity record. Files are parsed server-side on upload, so you do not need any special software beyond a spreadsheet application to produce them.

Large files are handled in batches, so a file with tens of thousands of rows uploads and validates without you doing anything differently.

## The fields

Your data uses the standard sexual health reporting fields — the same currencies, activity codes and patient fields defined in the national **GUMCAD** and **SRHAD** datasets — plus any **local codes** your commissioner has asked you to include for activity the standard datasets do not cover (see [Grouper Rules](/sexual-health-tariff/grouper-rules) and [Technical Guidance](/sexual-health-tariff/technical-guidance)).

Every field in a submission carries three things the Grouper checks:

- a **value** — present where the field is mandatory;
- a **format** — the value matches the pattern expected for that field (a date, a code, a number);
- a **valid option** — where a field draws from a controlled list of codes, the value is one of them.

## How your file is checked

On upload, each cell is validated against its field definition. A record fails validation for one of three reasons:

| Check | What it means | Example message |
|-------|---------------|-----------------|
| Mandatory | A required field is empty | *"&lt;field&gt; is mandatory and cannot be empty"* |
| Format | The value does not match the field's required pattern | *"Value &lt;x&gt; does not match required format"* |
| Valid option | The value is not in the field's list of allowed codes | *"&lt;x&gt; is not a valid option for this field"* |

A file with any validation errors cannot be submitted until those errors are cleared. The [File Validation](/sexual-health-tariff/file-validation-process) page explains how errors are reported and how to fix them.

## Before you upload — a checklist

- One file (or set of files) per provider, per month.
- Header row present and correctly named.
- Mandatory fields populated on every record.
- Codes drawn from the current GUMCAD / SRHAD lists, plus any agreed local codes.
- Clinic identifiers match clinics known to the Grouper (new clinics need an address and host commissioner — see the [Submission Process](/sexual-health-tariff/grouper-submission-process)).

{{segment:copyright:link-modal}}
