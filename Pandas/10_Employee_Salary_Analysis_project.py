import pandas as pd
import matplotlib.pyplot as plt

# ======================================
# Employee Salary Analysis
# Author: Your Name
# ======================================

# Load Dataset
df = pd.read_excel("employee_salary_dataset.xlsx")

# ======================================
# Data Cleaning
# ======================================

# Fill missing values
df["Age"] = df["Age"].fillna(round(df["Age"].mean()))
df["Salary"] = df["Salary"].fillna(round(df["Salary"].median()))

# Fix invalid Age values
df.loc[
    (df["Age"] < 18) | (df["Age"] > 65),
    "Age"
] = round(df["Age"].mean())

# Fix negative Salary values
df.loc[
    df["Salary"] < 0,
    "Salary"
] = round(df["Salary"].median())

# Fix invalid Experience values
df.loc[
    df["Experience_Years"] > 45,
    "Experience_Years"
] = round(df["Experience_Years"].median())

# Fill missing Department values
df["Department"] = df["Department"].fillna(
    df["Department"].mode()[0]
)

# Standardize Department names
df["Department"] = df["Department"].replace({
    "Hr": "HR",
    "H R": "HR",
    "Human Resource": "HR"
})

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert Joining Date
df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    format="mixed"
)

# Save cleaned dataset
df.to_excel("employee_salary_cleaned.xlsx", index=False)

# ======================================
# Exploratory Data Analysis (EDA)
# ======================================

print("\nFirst 10 Records")
print(df.head(10))

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())

print("\nDepartment Count")
print(df["Department"].value_counts())

print("\nAverage Salary by Department")
print(df.groupby("Department")["Salary"].mean())

print("\nAverage Salary by City")
print(df.groupby("City")["Salary"].mean())

print("\nCorrelation Matrix")
print(df.corr(numeric_only=True))

# ======================================
# Data Visualization
# ======================================

# Average Salary by Department
dept_salary = df.groupby("Department")["Salary"].mean()

dept_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.grid(True)
plt.tight_layout()
plt.show()

# Salary Distribution
df["Salary"].plot(kind="hist", bins=20)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()

# Employees by Department
df["Department"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Employees by Department")
plt.tight_layout()
plt.show()

# Experience vs Salary
plt.scatter(
    df["Experience_Years"],
    df["Salary"],
    alpha=0.7
)
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.show()

# Salary by Department
df.boxplot(
    column="Salary",
    by="Department",
    rot=45
)
plt.title("Salary by Department")
plt.suptitle("")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()

print("\nProject Completed Successfully!")
