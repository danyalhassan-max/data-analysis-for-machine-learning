# ==========================================
# File Name : student_marks_numpy.py
# Author    : Danyal Hassan
# Description:
# This program demonstrates basic NumPy array
# operations such as indexing, slicing,
# filtering, sorting, copying, reshaping,
# iterating, splitting, and concatenating.
# ==========================================

import numpy as np

# -------------------------------
# Create a 2D NumPy array
# -------------------------------
student_marks = np.array([
    [30, 93, 45, 76],
    [62, 54, 78, 46],
    [25, 76, 34, 65],
    [73, 25, 75, 58],
    [53, 43, 65, 69]
])

# -------------------------------
# Array Information
# -------------------------------
print("Student Marks:\n", student_marks)

print("\nNumber of Dimensions:", student_marks.ndim)
print("Shape of Array:", student_marks.shape)
print("Total Elements:", student_marks.size)
print("Data Type:", student_marks.dtype)

# -------------------------------
# Indexing and Slicing
# -------------------------------
print("\nMarks of Student 3:")
print(student_marks[2])

print("\nSecond Column (Subject 2 Marks):")
print(student_marks[:, 1])

print("\nFirst 3 Students and First 2 Subjects:")
print(student_marks[0:3, 0:2])

# -------------------------------
# Find Specific Value
# -------------------------------
print("\nPosition of Marks = 25:")
print(np.where(student_marks == 25))

# -------------------------------
# Boolean Filtering
# -------------------------------
filter_arr = student_marks > 80

print("\nBoolean Mask:")
print(filter_arr)

new_arr = student_marks[filter_arr]

print("\nMarks Greater Than 80:")
print(new_arr)

# -------------------------------
# Sorting
# -------------------------------
print("\nSorted Marks of First Student:")
print(np.sort(student_marks[0]))

# -------------------------------
# Copy vs Original Array
# -------------------------------
copy_arr = student_marks.copy()
copy_arr[0, 0] = 100

print("\nOriginal Array:")
print(student_marks)

print("\nCopied Array (Modified):")
print(copy_arr)

# -------------------------------
# Reshape Array
# -------------------------------
reshaped_arr = student_marks.reshape(20)

print("\nReshaped Array (1D):")
print(reshaped_arr)

# -------------------------------
# Iterate Through Array Elements
# -------------------------------
print("\nIterating Through All Marks:")

for mark in np.nditer(student_marks):
    print(mark)

# -------------------------------
# Split Array
# -------------------------------
split_arr = np.array_split(student_marks, 2)

print("\nFirst Split:")
print(split_arr[0])

print("\nSecond Split:")
print(split_arr[1])

# -------------------------------
# Join Arrays
# -------------------------------
join_arr = np.concatenate((split_arr[0], split_arr[1]))

print("\nJoined Array:")
print(join_arr)
