"""
NumPy Array Fundamentals

Covers:
- Creating NumPy arrays
- ndarray type
- Arrays from lists and tuples
- 0-D, 1-D, 2-D, and 3-D arrays
- Custom dimensions using ndmin
- ndim attribute
"""

import numpy as np


# Create a NumPy array from a list
arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("Array type:", type(arr))


# Create an array from a tuple
tuple_arr = np.array((1, 2, 5, 6))

print("\nArray from tuple:", tuple_arr)


# 0-D array
zero_dim_arr = np.array(42)

print("\n0-D Array:", zero_dim_arr)
print("Dimensions:", zero_dim_arr.ndim)


# 1-D array
one_dim_arr = np.array([1, 6, 4, 3, 5])

print("\n1-D Array:", one_dim_arr)
print("Dimensions:", one_dim_arr.ndim)


# 2-D array
two_dim_arr = np.array([
    [8, 5, 7, 3],
    [3, 4, 2, 6]
])

print("\n2-D Array:")
print(two_dim_arr)
print("Dimensions:", two_dim_arr.ndim)


# 3-D array
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
print("Dimensions:", three_dim_arr.ndim)


# Create an array with five dimensions
five_dim_arr = np.array([1, 2, 3, 4], ndmin=5)

print("\n5-D Array:")
print(five_dim_arr)
print("Dimensions:", five_dim_arr.ndim)
