# CleanX — Smart CSV Data Cleaning Tool

CleanX is a Python-based web application that helps users clean CSV datasets, identify common data-quality issues, and download cleaned data with a quality report. It is built using Python, Pandas, and Streamlit.

## Features

- **CSV Upload:** Upload your own CSV dataset.
- **Data Preview:** View your dataset before cleaning.
- **Missing Value Detection:** Identify missing values in columns.
- **Duplicate Detection:** Find duplicate records and remove them.
- **Whitespace Cleaning:** Remove unnecessary leading and trailing whitespace from text values.
- **Missing Value Handling:** Choose an available strategy for handling missing values.
- **Data Quality Statistics:** Compare dataset quality before and after cleaning.
- **Download Cleaned CSV:** Export the cleaned dataset.
- **Quality Report:** Download a report containing data-quality statistics.

## Tech Stack

- Python
- Pandas
- NumPy
- Streamlit

## Project Structure

```text
CleanX_Project/
├── app.py
├── cleaner.py
├── requirements.txt
├── sample_data.csv
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/arunsinghtomar/CleanX.git
cd CleanX
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, run this command for the current terminal session and try activating again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## How to Use

1. Start the CleanX application.
2. Upload a CSV file.
3. Preview the dataset and inspect data-quality statistics.
4. Choose the available cleaning options.
5. Apply the cleaning operations.
6. Review the updated statistics.
7. Download the cleaned CSV and quality report.

## Sample Dataset

A sample CSV file, `sample_data.csv`, is included for testing the application. You can also upload your own CSV dataset.

**Tip:** Keep a copy of your original dataset before applying cleaning operations.

## Learning Outcomes

This project demonstrates practical experience with:

- Python programming and modular code
- Data manipulation using Pandas
- Handling missing values and duplicate records
- CSV file processing
- Building interactive web applications with Streamlit
- Creating downloadable data-quality reports

## Future Improvements

- Add support for Excel files
- Add customizable column-level cleaning rules
- Add more data-quality visualizations
- Add automated data-type detection
- Add additional export formats

## Author

**Arun Singh Tomar**

- GitHub: [@arunsinghtomar](https://github.com/arunsinghtomar)
- LinkedIn: [Arun Singh Tomar](https://www.linkedin.com/in/arun-singh-tomar-2576162b9/)

## License

This project is available for learning and portfolio purposes. If you want others to reuse or modify it under explicit terms, consider adding an MIT License file.
