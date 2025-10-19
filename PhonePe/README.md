# PhonePe Pulse — Project Overview

This repository contains analysis and a Streamlit dashboard for PhonePe Pulse data. It includes data processing notebooks, a Streamlit app, and helper functions to load data and push/pull from a MySQL database.

This project has analysis done on Phonepe pulse data available on GitHub repository

---

## Folderel structure

- `Streamlit_App/` — Folder for Streamlit dashboard app and functions.
  - `PhonePay_Pulse.py` — main Streamlit app python file (run this with Streamlit).
  - `Functions/` — Folder to store all the functions used in the project.
    - `config.py` — file to import all the libraries.
    - `Data_Loader.py` — Function to run sql codes and return the dataframe of sql query.
    - `State_Map.py`, Contains cleanmapping for state names.
    - `Test_Notebook.ipynb` — dev notebook used for ad-hoc testing.
- `Data Processing/` — scripts and notebooks to parse the PhonePe Pulse GitHub JSON files and output processed CSVs.
  - `Code/` — processing notebooks and scripts (e.g., `Data_Load_Push.ipynb`).
  - `Files/` — contains raw and processed data (Processed_Data/ with CSV outputs).
- `Archive/` 
- `requirements.txt` — Python dependencies (install into your virtual environment).
- `India_Map_New.geojson` — GeoJSON used for India map visualizations.

---

## Quick setup

1. Create and activate a virtual environment (PowerShell example):

```powershell
python -m venv C:\path\to\venv
# activate
& 'C:\path\to\venv\Scripts\Activate.ps1'
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Copy or create a `.env` file in the project root with the following variables (example):

```
MY_SQL_HOST=localhost
MY_SQL_USER=root
MY_SQL_PASSWORD=your_password
MY_SQL_PORT=3306
```


---

## How to run the Streamlit app

From the project root (PowerShell):

```powershell
# Activate venv (optional)
& 'C:\path\to\venv\Scripts\Activate.ps1'
# Run the app
streamlit run "Streamlit_App\PhonePay_Pulse.py"

---

## Database integration

- The project uses MySQL for storing processed tables (e.g., `aggregated_trans`, `aggregated_insurance`, `aggregated_user`, `map_*`, `top_*`).
- `Functions/Data_Loader.py` provides `sql_query_runner(query, params)` that returns a pandas DataFrame.
- The Streamlit app calls `sql_query_runner(query)` to load data; the function constructs a SQLAlchemy engine using environment variables and runs the query using `text(query)` and `engine.connect()`.

Notes:
- SQLAlchemy 2.0 compatibility is required. The code uses `with engine.connect() as conn:` and `conn.execute(text(query), params)`.
- If your password contains special characters, the project uses safe URL creation/quoting in some places — prefer setting environment variables and using `sql_query_runner` rather than hardcoding credentials.

