# Grouper Rules

The Grouper follows a set of rules that reflect the underlying ruleset for the tariff.

## File Upload

The Grouper will accept csv or xlsx files of any length that conform to one of the two [datasets] (/dataset).

File layout GUMCADv2 and SRHAD files are generally episode based with one row per episode.  Both file formats expect to receive a number of activity codes SHAPPT and SRH Care Activity codes in the fields provided in the row of data.

The Grouper accepts a merged set of GUMCADv2 and SRHAD data that combines common demographic data alongside the GU and SRH specific fields, see [datasets] (/dataset) for more details.

Whereas GUMCADv3 has one Episode_Activity field and episodes with multiple Episode_Activity entries are represented in multiple rows of data (this usually entails repeating the standard demographic data for each record).

Local Codes are provided to record activity we need to track for specific tariffs.  Each tariff configuration will list all the local codes used in that configuration.  Generally, the local codes are associated with SHHAPT, SRH Care Activity or Episode_Activity fields (ie the field that records the activity). Occasionally, we issue a local code for another field - the tariff configuration local code list will specify which field the local code is associated with.

File naming conventions.  The Grouper will only accept file names under 50 characters long and with a single '.' in the name.  

    Acceptable: 
        
        - my file.csv
        - your_file.xlsx

    Not acceptable:

        - my file my file my file my file my file my filemy file my file.csv
        -myfile.myfile.xlsx


File data structure. Both csv and xlsx files should have one worksheet (the Grouper will only read the first worksheet). Data should start at cell A1 and row 1 should contain a contiguous list of headings, the first column with an empty heading will considered the end of the column headings and no further columns will be read.  Similarly, data should start in the row directly below the column headings and continue contiguously to the lst row of data, any empty rows will be considered to indicate the last row of data and no further rows will be read.  To prevent errors make sure there is no 'loose' data below or to the right of your dataset.

Troubleshooting.  When an upload fails, the first response is to cut and 'paste special' as values the entire dataset into a new clean worksheet and save it.

Date formats.  To ensure date alignment across varying operating systems and legacy versions of Microsoft Excel, the ingest engine dynamically adapts to the workbook's root properties. The platform explicitly supports both the ISO/IEC 29500 1900 Date System and the 1904 Date System.

All dates should be ISO 8601 standard formatted: YYYY-MM-DD this is particularly important for csv files that cannot rely on embedded formatting.  Data must be localized to a UTC/GMT baseline or given a specific timezone markers if using string timestamps.  In Excel date columns must be explicitly formatted as a 'Date' or 'Short Date' category in Excel. Avoid mixing text strings and native dates in the same column.

Long Integers.  Excel operates strictly under the IEEE 754 double-precision floating-point standard, which mandates a maximum numeric precision limit of 15 digits. When a number like 1086331000000100 (16 digits) is evaluated as a pure number, Excel automatically truncates the 16th digit to a zero and displays it as 1.08633E+15. GUMCADv3 has several fields that rely on long integers. To prevent data corruption caused by the standard IEEE 754 15-digit precision limit in Microsoft Excel, all GUMCADv3 fields containing numeric identifiers longer than 15 digits must be explicitly defined and saved as text strings.  Using the ' qualifier can achieve this, '1086331000000100 will be read as text.

Field matching. When a file is uploaded, the Grouper inspects the column headings and then attempts to match those headings to the fields expected for the type of file selected.  Users should check each column headings is properly matched to a field.

Minimum dataset. Each record in each file must have a valid patient_id, clinic_id and attendance_date or consultation_date field.

## File Validation

Valid data

New clinic ids

LSOAs

## File Processing

Key:Value pairs

Row identifier

Episode identifier

Handling merging, overwriting and duplicate data

## Submission

Remove prior charges and KPIs

Identify current tariff configuration for provider and submission

Identify triggered currencies, (one per episode)

Resolve any invalid currency combinations

Allocate tariff rates to currencies (with one primary rate per episode)

Allocate commissioners per currency charged according to currency cross-charging rules

Calculate KPIs

## Resets

Resets Request