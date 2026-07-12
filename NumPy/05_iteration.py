"""
NumPy Array Iteration

Covers:
- Iterating over 1-D arrays
- Iterating over 2-D arrays
- Nested iteration
- np.nditer()
- Buffered iteration with data type conversion
- np.ndenumerate()
"""

import numpy as np


# Iterate over a 1-D array
one_dim_arr = np.array([1, 2, 4, 3])

print("1-D Array Elements:")

for element in one_dim_arr:
    print(element)


# Iterate over a 2-D array
two_dim_arr = np.array([
    [1, 4, 7, 4],
    [7, 4, 6, 2]
])

print("\n2-D Array Elements:")

for row in two_dim_arr:
    for element in row:
        print(element)


# Iterate over a 3-D array using nditer()
three_dim_arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\n3-D Array Elements using nditer:")

for element in np.nditer(three_dim_arr):
    print(element)


# Iterate with buffered data type conversion
arr = np.array([1, 2, 3])

print("\nBuffered String Conversion:")

for element in np.nditer(
    arr,
    flags=["buffered"],
    op_dtypes=["S"]
):
    print(element)


# Enumerate a 1-D array
print("\n1-D Array Indexes and Values:")

for index, value in np.ndenumerate(arr):
    print(index, value)


# Enumerate a 2-D array
two_dim_arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print("\n2-D Array Indexes and Values:")

for index, value in np.ndenumerate(two_dim_arr):
    print(index, value)
