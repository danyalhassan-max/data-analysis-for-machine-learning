import pandas as pd

df = pd.read_csv("data.csv")
print(df.to_string())

pd.options.display.max_rows = 78

print(df)

df = pd.read_json("data.json")
print(df.to_string())

df = pd.read_excel("student_cleaning_dataset.xlsx")
print(df)
