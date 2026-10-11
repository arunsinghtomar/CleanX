# CleanX — Smart Data Cleaning Tool

CleanX is a beginner-friendly Python web app for inspecting and cleaning CSV datasets. It helps users identify missing values and duplicate rows, trim extra spaces, apply selected cleaning strategies, and export the cleaned dataset plus a before/after quality report.

## Features
- Upload and preview CSV files
- View row, column, missing-value, and duplicate-row counts
- Inspect missing values by column
- Remove duplicate rows and trim whitespace
- Choose how to handle missing values
- Review a cleaning log and download cleaned CSV data
- Download a before/after data quality report

## Tech stack
- Python
- Pandas
- Streamlit

## Project structure
```text
CleanX/
├── app.py
├── cleaner.py
├── requirements.txt
├── sample_data.csv
├── README.md
└── .gitignore
```

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create a virtual environment (recommended):

   **Windows PowerShell**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```
6. Open the local address shown in your terminal.

## How to use
1. Upload a CSV file or use the included sample dataset.
2. Review the preview and quality metrics.
3. Select cleaning options.
4. Click **Clean dataset**.
5. Download the cleaned CSV and quality report.

## Important notes
Cleaning choices can change a dataset's meaning. Review your data and choose a strategy appropriate for your use case. This is a learning/demo tool, not a replacement for validating critical production data.

## Future improvements
- Data quality charts
- Column type validation and date parsing
- Undo cleaning actions
- PDF reports and custom cleaning rules

## Author
**Arun Singh Tomar**
- GitHub: https://github.com/arunsinghtomar
- LinkedIn: https://www.linkedin.com/in/arun-singh-tomar-2576162b9/
