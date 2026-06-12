# How-To Guides

This page provides step-by-step instructions for common workflows in the Sexual Health Tariff Grouper application. Click any screenshot to view an enlarged version.

---

## Data Upload

Follow these steps to upload your activity data file to the Tariff Grouper for processing.

### Step 1: Navigate to the Data Upload Page

From the Tariff Grouper dashboard, select **Data Upload** from the main navigation menu. This opens the upload interface where you can submit your activity data file for tariff processing.

<img src="assets/images/how-to/data-upload/step-1-navigate.png" alt="Tariff Grouper dashboard showing the Data Upload option highlighted in the main navigation menu" loading="lazy">

*The Data Upload option is accessible from the main navigation menu on the Tariff Grouper dashboard.*

### Step 2: Select and Upload Your Data File

Click the **Choose File** button to open the file picker. Select your prepared CSV data file from your local machine. Ensure the file follows the required format as described in the [Technical Guidance](/sexual-health-tariff/technical-guidance) section. Once selected, click **Upload** to submit the file.

<img src="assets/images/how-to/data-upload/step-2-select-file.png" alt="File selection dialog with the Choose File button and Upload button highlighted" loading="lazy">

*Use the Choose File button to select your CSV, then click Upload to submit it for processing.*

### Step 3: Confirm Upload and Review Validation

After uploading, the system validates your data file against the expected format and field specifications. A summary screen displays the validation outcome, including the number of records accepted, any validation errors, and warnings. Review the results and resolve any errors before proceeding.

<img src="assets/images/how-to/data-upload/step-3-confirm-validation.png" alt="Upload validation summary showing accepted records count, errors, and warnings" loading="lazy">

*The validation summary confirms how many records were accepted and highlights any issues to resolve.*

### Step 4: Submit for Processing

Once validation passes with no blocking errors, click **Submit for Processing** to queue your data for tariff calculation. You will receive a confirmation message with a reference number for tracking.

<img src="assets/images/how-to/data-upload/step-4-submit-processing.png" alt="Submit for Processing button and confirmation message with reference number" loading="lazy">

*Click Submit for Processing to queue your validated data for tariff calculation.*

---

## Tariff Calculation

Follow these steps to run a tariff calculation against your uploaded activity data.

### Step 1: Open the Tariff Calculation Module

From the main navigation, select **Tariff Calculation**. This opens the calculation interface where you can configure and run tariff calculations against your uploaded data submissions.

<img src="assets/images/how-to/tariff-calculation/step-1-open-module.png" alt="Main navigation with Tariff Calculation option highlighted" loading="lazy">

*Select Tariff Calculation from the main navigation to access the calculation interface.*

### Step 2: Select the Configuration and Data Period

Choose the applicable **Tariff Configuration** from the dropdown list. This determines the tariff rules and rates that will be applied to your data. Then select the **data period** (date range) for the calculation. Only uploaded data within this period will be included.

<img src="assets/images/how-to/tariff-calculation/step-2-select-configuration.png" alt="Configuration dropdown and date period selector with available options displayed" loading="lazy">

*Select your tariff configuration and the date range covering the activity data you wish to calculate.*

### Step 3: Run the Calculation

Click **Run Calculation** to begin processing. The system applies the selected tariff rules to each activity record, grouping activities into tariff bands and calculating the associated costs. A progress indicator shows the calculation status.

<img src="assets/images/how-to/tariff-calculation/step-3-run-calculation.png" alt="Run Calculation button and progress indicator showing calculation in progress" loading="lazy">

*The progress indicator shows the status of your tariff calculation as it processes each record.*

### Step 4: Review Calculation Results

Once complete, the results screen displays a summary of the calculation including total cost, number of activities grouped, and a breakdown by tariff band. You can download the detailed results or proceed to generate reports.

<img src="assets/images/how-to/tariff-calculation/step-4-review-results.png" alt="Calculation results summary showing total cost, activity count, and tariff band breakdown" loading="lazy">

*Review the calculation summary including total cost and breakdown by tariff band.*

---

## Report Generation

Follow these steps to generate and download reports from your tariff calculation results.

### Step 1: Navigate to Reports

From the main navigation, select **Reports**. Alternatively, click **Generate Report** from the calculation results screen. The reports interface lists available report types for your completed calculations.

<img src="assets/images/how-to/report-generation/step-1-navigate-reports.png" alt="Reports option in main navigation and the reports interface showing available report types" loading="lazy">

*Access the Reports section from the main navigation or directly from calculation results.*

### Step 2: Select Report Type and Parameters

Choose the report type you require from the available options (e.g., Summary Report, Detailed Activity Report, KPI Report). Configure any additional parameters such as date range, provider filter, or output format (PDF or CSV).

<img src="assets/images/how-to/report-generation/step-2-select-report-type.png" alt="Report type selection showing available options and configuration parameters" loading="lazy">

*Choose your report type and configure parameters such as date range and output format.*

### Step 3: Generate the Report

Click **Generate Report** to create your report. The system compiles the data based on your selected parameters. For large datasets, report generation may take a few moments — a progress indicator will show the current status.

<img src="assets/images/how-to/report-generation/step-3-generate-report.png" alt="Generate Report button with progress indicator showing report compilation status" loading="lazy">

*Click Generate Report and wait for the progress indicator to confirm completion.*

### Step 4: Download or Share the Report

Once generated, the report appears in your reports list with a **Download** button. Click Download to save the report to your local machine. Reports are available in the format you selected (PDF or CSV) and remain accessible from the reports list for future reference.

<img src="assets/images/how-to/report-generation/step-4-download-report.png" alt="Completed report in the reports list with Download button highlighted" loading="lazy">

*Download your completed report or access it later from the reports list.*
