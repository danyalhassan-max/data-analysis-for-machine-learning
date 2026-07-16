import pandas as pd

df = pd.read_excel("student_cleaning_dataset_v2.xlsx")

df.loc[df["Age"] > 80, "Age"] = 23

df.loc[df["Math"] > 100, "Math"] = 100

df.loc[df["Science"] < 0, "Science"] = 0

df.loc[df["English"] < 0, "English"] = 0

df.loc[df["Attendance"] > 100, "Attendance"] = 100

print(df)
