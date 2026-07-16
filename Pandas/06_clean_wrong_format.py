import pandas as pd

df = pd.read_excel("student_cleaning_dataset_v2.xlsx")

df["Admission_Date"] = pd.to_datetime(
    df["Admission_Date"],
    format="mixed",
    errors="coerce"
)

df.dropna(
    subset=["Admission_Date"],
    inplace=True
)

print(df)
