import pandas as pd

data = {
    "Calories": [1, 230, 456],
    "Duration": [34, 45, 39]
}

df = pd.DataFrame(data)

print(df)

print(df.loc[[0, 1]])

df = pd.DataFrame(
    data,
    index=["day1", "day2", "day3"]
)

print(df)

print(df.loc["day1"])
