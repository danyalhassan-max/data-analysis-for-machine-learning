"""
NumPy Array Indexing and Slicing

Covers:
- 1-D indexing
- 2-D indexing
- 3-D indexing
- Array slicing
- Step slicing
- Row and column selection
"""

import numpy as np


# 1-D array indexing
one_dim_arr = np.array([1, 6, 4, 3, 5])

print("1-D Array:", one_dim_arr)
print("First element:", one_dim_arr[0])
print("Second + fourth element:", one_dim_arr[1] + one_dim_arr[3])


# 1-D array slicing
print("\nFirst two elements:", one_dim_arr[0:2])
print("Slice with step:", one_dim_arr[1:4:2])


# 2-D array
two_dim_arr = np.array([
    [8, 5, 7, 3],
    [3, 4, 2, 6]
])

print("\n2-D Array:")
print(two_dim_arr)

print("First row, fourth element:", two_dim_arr[0, 3])
print("Second row, third element:", two_dim_arr[1, 2])

# Select part of the first row
print("First row, index 1 to 2:", two_dim_arr[0, 1:3])

# Select the third column from both rows
print("Third column:", two_dim_arr[0:2, 2])


# 3-D array indexing
three_dim_arr = np.array([
    [
        [8, 5, 7, 3],
        [3, 4, 2, 6]
    ],
    [
        [4, 8, 3, 2],
        [8, 4, 7, 3]
    ]
])

print("\n3-D Array:")
print(three_dim_arr)

print(
    "Selected 3-D element:",
    three_dim_arr[0, 1, 3]
)
