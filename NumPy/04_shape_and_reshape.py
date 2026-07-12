"""
NumPy Array Shape and Reshape

Covers:
- shape attribute
- Shape of multidimensional arrays
- Shape of arrays created with ndmin
- Reshaping 1-D arrays into 2-D and 3-D arrays
"""

import numpy as np


# Check the shape of a 2-D array
two_dim_arr = np.array([
    [1, 4, 6, 3],
    [3, 5, 4, 1]
])

print("2-D Array:")
print(two_dim_arr)
print("Shape:", two_dim_arr.shape)


# Shape of a five-dimensional array
five_dim_arr = np.array([2, 6, 4, 2], ndmin=5)

print("\n5-D Array:")
print(five_dim_arr)
print("Shape:", five_dim_arr.shape)


# Reshape a 1-D array into a 2-D array
arr = np.array([
    1, 2, 3, 4, 5, 6,
    7, 8, 9, 10, 11, 12
])

reshaped_2d_arr = arr.reshape(4, 3)

print("\nReshaped 2-D Array:")
print(reshaped_2d_arr)
print("Shape:", reshaped_2d_arr.shape)


# Reshape a 1-D array into a 3-D array
reshaped_3d_arr = arr.reshape(2, 3, 2)

print("\nReshaped 3-D Array:")
print(reshaped_3d_arr)
print("Shape:", reshaped_3d_arr.shape)
