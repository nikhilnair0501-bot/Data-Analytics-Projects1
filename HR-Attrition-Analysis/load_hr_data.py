# Load HR Attrition data into MySQL

import pandas as pd

df = pd.read_csv("D:\\Nikhil\\DataAnalytics\\HR_Attrition\\archive\\HR-Employee-Attrition.csv")
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@1234",
    database="superstore"
)

cursor = conn.cursor()

# Create HR table
cursor.execute("DROP TABLE IF EXISTS hr_attrition;")
cursor.execute("""
    CREATE TABLE hr_attrition (
        Age INT,
        Attrition VARCHAR(5),
        BusinessTravel VARCHAR(50),
        Department VARCHAR(50),
        JobRole VARCHAR(50),
        JobSatisfaction INT,
        MonthlyIncome INT,
        OverTime VARCHAR(5),
        PerformanceRating INT,
        TotalWorkingYears INT,
        WorkLifeBalance INT,
        YearsAtCompany INT
    )
""")

# Insert data
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO hr_attrition 
        (Age, Attrition, BusinessTravel, Department, JobRole, 
         JobSatisfaction, MonthlyIncome, OverTime, PerformanceRating,
         TotalWorkingYears, WorkLifeBalance, YearsAtCompany)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (row["Age"], row["Attrition"], row["BusinessTravel"],
          row["Department"], row["JobRole"], row["JobSatisfaction"],
          row["MonthlyIncome"], row["OverTime"], row["PerformanceRating"],
          row["TotalWorkingYears"], row["WorkLifeBalance"], row["YearsAtCompany"]))

conn.commit()
print("HR data loaded! Rows:", len(df))
conn.close()