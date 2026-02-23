# Financial ETL Pipeline (Python + MySQL)

## Overview  
Built an end-to-end ETL pipeline that processes monthly financial Excel files, loads the data into a MySQL database, and generates automated summary reports using SQL.

---

## What This Project Does

- Reads multiple Excel files (Jan–Mar 2025)  
- Loads structured data into MySQL  
- Prevents duplicate data during re-runs  
- Performs SQL aggregation (Revenue, Transactions, Errors)  
- Generates automated Excel report from database  

---

## Tech Stack

- Python (pandas)  
- MySQL  
- SQL  
- openpyxl  

---

## Project Flow

Excel Files → Python → MySQL Database → SQL Query → Excel Report

---

## How to Run

1. Install dependencies  

```
pip install -r requirements.txt
```

2. Create database in MySQL  

```
CREATE DATABASE financial_etl;
```

3. Update MySQL credentials in `automation.py`

4. Run script  

```
python automation.py
```

---

## Output

- MySQL table with processed financial data  
- Automated financial summary report (`mysql_financial_report.xlsx`)
