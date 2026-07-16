import pandas as pd

df = pd.read_excel("student_cleaning_dataset.xlsx")

print(df)

# Remove Empty Rows
print(df.dropna())

# Fill All Empty Values
filled = df.fillna(20)
print(filled)

# Fill Specific Columns
filled = df.fillna({
    "Age": 20,
    "Science": 75
})

print(filled)

# Mean
df["Age"] = df["Age"].fillna(
    round(df["Age"].mean())
)

df["Science"] = df["Science"].fillna(
    round(df["Science"].mean())
)

# Median
df["Age"] = df["Age"].fillna(
    round(df["Age"].median())
)

df["Science"] = df["Science"].fillna(
    round(df["Science"].median())
)

# Mode
df["Age"] = df["Age"].fillna(
    df["Age"].mode()[0]
)

df["Science"] = df["Science"].fillna(
    df["Science"].mode()[0]
)

print(df)
