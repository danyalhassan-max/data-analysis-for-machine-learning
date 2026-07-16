import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

print(df.head(10))

print(df.tail())

df.info()

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.describe())
