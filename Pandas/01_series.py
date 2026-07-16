import pandas as pd

cars = ["BMW", "Volvo", "Ford"]
passings = [3, 7, 2]

mydataset = {
    "cars": cars,
    "passings": passings
}

df = pd.DataFrame(mydataset)
print(df)

numbers = [1, 3, 6, 8]

series = pd.Series(numbers, index=["a", "b", "c", "d"])
print(series)
print(series["b"])

calories = {
    "day1": 480,
    "day2": 390,
    "day3": 290
}

series = pd.Series(calories, index=["day1", "day2"])
print(series)
