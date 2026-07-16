import pandas as pd

df = pd.read_excel("student_cleaning_dataset_v2.xlsx")

print(df.duplicated())

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df.to_excel(
    "Cleaned.xlsx",
    index=False
)

print(df)
