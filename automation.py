import pandas as pd
import mysql.connector
import os
if __name__ == "__main__":

# MySQL connection settings
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123abc",
    "database": "financial_etl"
}

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

print("Connected to MySQL database.")

# Create table
create_table_query = """
CREATE TABLE IF NOT EXISTS financial_data (
    Date DATE,
    Employee VARCHAR(100),
    Department VARCHAR(100),
    Region VARCHAR(50),
    Transactions INT,
    Revenue_USD FLOAT,
    Errors INT,
    Hours_Worked FLOAT
)
"""
cursor.execute(create_table_query)

# Clear existing data before inserting new data
cursor.execute("TRUNCATE TABLE financial_data;")
print("Old data cleared.")

print("Table ready.")

# Folder containing Excel files
data_folder = "data"

# Process each file
for file in os.listdir(data_folder):
    if file.endswith(".xlsx"):
        
        file_path = os.path.join(data_folder, file)
        print(f"Processing {file}")
        
        df = pd.read_excel(file_path)
        
        # Insert data into MySQL
        for _, row in df.iterrows():
            
            insert_query = """
            INSERT INTO financial_data
            (Date, Employee, Department, Region, Transactions, Revenue_USD, Errors, Hours_Worked)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(insert_query, (
                row["Date"],
                row["Employee"],
                row["Department"],
                row["Region"],
                row["Transactions"],
                row["Revenue_USD"],
                row["Errors"],
                row["Hours_Worked"]
            ))

conn.commit()
print("Data loaded into MySQL.")

# Run SQL query to generate summary
summary_query = """
SELECT Department,
       SUM(Revenue_USD) AS Total_Revenue,
       SUM(Transactions) AS Total_Transactions,
       SUM(Errors) AS Total_Errors
FROM financial_data
GROUP BY Department;
"""

summary_df = pd.read_sql(summary_query, conn)

# Save report
output_path = "output/mysql_financial_report.xlsx"
summary_df.to_excel(output_path, index=False)

print("Report generated:", output_path)

# Close connection
cursor.close()
conn.close()

print("ETL automation completed.")
