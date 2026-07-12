"""
NumPy Data Types, Copy, and View

Covers:
- Defining array data types
- dtype attribute
- astype() conversion
- Integer, float, string, and Boolean conversion
- Array copy
- Array view
- base attribute
"""

import numpy as np


# Array with byte string data type
string_arr = np.array([1, 5, 3, 7], dtype="S")

print("Byte String Array:", string_arr)
print("Data type:", string_arr.dtype)


# Array with 4-byte integer data type
integer_arr = np.array([2, 5, 4, 8], dtype="i4")

print("\nInteger Array:", integer_arr)
print("Data type:", integer_arr.dtype)


# Convert float array to integer
float_arr = np.array([1.1, 4.2, 6.3])

converted_int_arr = float_arr.astype("i")
converted_int_arr_alt = float_arr.astype(int)

print("\nOriginal Float Array:", float_arr)
print("Converted Integer Array:", converted_int_arr)
print("Converted using int:", converted_int_arr_alt)
print("Converted data type:", converted_int_arr.dtype)


# Convert integer array to Boolean
number_arr = np.array([0, 1, 5, -2])

boolean_arr = number_arr.astype(bool)

print("\nOriginal Array:", number_arr)
print("Boolean Array:", boolean_arr)
print("Boolean data type:", boolean_arr.dtype)


# Array copy
original_arr = np.array([1, 4, 3, 2, 6])
copied_arr = original_arr.copy()

original_arr[0] = 42
copied_arr[0] = 31

print("\nOriginal Array after modification:", original_arr)
print("Copied Array after modification:", copied_arr)


# Array view
original_view_arr = np.array([1, 4, 3, 2, 6])
view_arr = original_view_arr.view()

original_view_arr[0] = 2
view_arr[1] = 43

print("\nOriginal Array:", original_view_arr)
print("View Array:", view_arr)


# Check ownership using base
base_arr = np.array([1, 2, 3, 4, 5])

copied_arr = base_arr.copy()
view_arr = base_arr.view()

print("\nCopy base:", copied_arr.base)
print("View base:", view_arr.base)
