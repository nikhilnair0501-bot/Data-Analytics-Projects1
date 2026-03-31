# HR Attrition Analysis — Layer 1: Python EDA
# Business Question: Why are employees leaving?
# Importing necessary libraries
from numpy import shape
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df = pd.read_csv("D:\\Nikhil\\DataAnalytics\\HR_Attrition\\archive\\HR-Employee-Attrition.csv")

# ===== EXPLORATION =====
print("----Shape----")
print(df.shape)

print("\n----Columns----")
print(df.columns.tolist())

print("\n----Attrition Value Counts----")
print(df["Attrition"].value_counts())

print("\n----Attrition Rates----")
Attrition_rate = df["Attrition"].value_counts(normalize=True) * 100
print(round(Attrition_rate, 2))

# ===== VISUALIZATION 1 — Attrition by Department =====
dept_attrition = df[df["Attrition"] == "Yes"].groupby("Department")["Attrition"].count()
dept_total = df.groupby("Department")["Attrition"].count()
dept_rate = round((dept_attrition / dept_total) * 100, 2)

plt.figure(figsize=(10, 6))
dept_rate.sort_values(ascending=False).plot(kind="bar", color="coral")
plt.title("Attrition Rate % by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate %")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.close()

# ===== VISUALIZATION 2 — Attrition by Job Role =====
role_attrition = df[df["Attrition"] == "Yes"].groupby("JobRole")["Attrition"].count()
role_total = df.groupby("JobRole")["Attrition"].count()
role_rate = (role_attrition / role_total * 100).round(2).sort_values(ascending=True)

plt.figure(figsize=(10, 8))
role_rate.plot(kind="barh", color="steelblue")
plt.title("Attrition Rate % by Job Role")
plt.xlabel("Attrition Rate %")
plt.tight_layout()
plt.show()
plt.close()

# ===== VISUALIZATION 3 IMPROVED — Overtime vs Attrition =====
overtime_rate = df[df["Attrition"] == "Yes"].groupby("OverTime")["Attrition"].count() / \
                df.groupby("OverTime")["Attrition"].count() * 100

plt.figure(figsize=(8, 6))
overtime_rate.plot(kind="bar", color=["steelblue", "coral"])
plt.title("Attrition Rate % by Overtime Status")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate %")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
plt.close()

# ===== VISUALIZATION 4 — Monthly Income vs Attrition =====
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Attrition", y="MonthlyIncome", palette=["steelblue", "coral"])
plt.title("Monthly Income Distribution by Attrition")
plt.xlabel("Attrition")
plt.ylabel("Monthly Income")
plt.tight_layout()
plt.show()
plt.close()

# ===== VISUALIZATION 5 — Age Group vs Attrition =====
# Create age groups
df["Age_Group"] = pd.cut(df["Age"],
                          bins=[18, 25, 35, 45, 60],
                          labels=["18-25", "26-35", "36-45", "46-60"])

age_attrition = df[df["Attrition"] == "Yes"].groupby("Age_Group", observed=True)["Attrition"].count()
age_total = df.groupby("Age_Group", observed=True)["Attrition"].count()
age_rate = (age_attrition / age_total * 100).round(2)

plt.figure(figsize=(10, 6))
age_rate.plot(kind="bar", color="mediumpurple")
plt.title("Attrition Rate % by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Attrition Rate %")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
plt.close()

overtime_check = df.groupby("OverTime")["Attrition"].value_counts(normalize=True) * 100
print(round(overtime_check, 2))