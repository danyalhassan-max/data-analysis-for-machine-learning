"""
NumPy Array Joining and Splitting

Covers:
- np.concatenate()
- np.stack()
- np.hstack()
- np.vstack()
- np.dstack()
- np.array_split()
"""

import numpy as np


first_arr = np.array([1, 2, 3, 4])
second_arr = np.array([4, 5, 6, 7])


# Concatenate arrays
concatenated_arr = np.concatenate((first_arr, second_arr))

print("Concatenated Array:")
print(concatenated_arr)


# Stack arrays along axis 1
stacked_arr = np.stack((first_arr, second_arr), axis=1)

print("\nStacked Array:")
print(stacked_arr)
print("Shape:", stacked_arr.shape)


# Horizontal stacking
horizontal_arr = np.hstack((first_arr, second_arr))

print("\nHorizontal Stack:")
print(horizontal_arr)
print("Shape:", horizontal_arr.shape)


# Vertical stacking
vertical_arr = np.vstack((first_arr, second_arr))

print("\nVertical Stack:")
print(vertical_arr)
print("Shape:", vertical_arr.shape)


# Depth stacking
depth_arr = np.dstack((first_arr, second_arr))

print("\nDepth Stack:")
print(depth_arr)
print("Shape:", depth_arr.shape)


# Split an array into three parts
split_arr = np.array_split(first_arr, 3)

print("\nSplit Arrays:")

for index, part in enumerate(split_arr):
    print(f"Part {index + 1}:", part)
