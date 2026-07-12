"""
NumPy Array Search, Sort, and Filter

Covers:
- np.where()
- Finding odd and even values
- np.searchsorted()
- np.sort()
- Boolean filtering
- Creating filter arrays
"""

import numpy as np


# Search for matching values
arr = np.array([1, 2, 3, 4, 5, 4, 4])

matching_indexes = np.where(arr == 4)

print("Indexes containing value 4:")
print(matching_indexes)


# Find odd and even value indexes
number_arr = np.array([4, 93, 22, 21, 18, 19, 52])

odd_indexes = np.where(number_arr % 2 == 1)
even_indexes = np.where(number_arr % 2 == 0)

print("\nOdd value indexes:", odd_indexes)
print("Even value indexes:", even_indexes)


# searchsorted() requires a sorted array
sorted_arr = np.array([4, 18, 19, 21, 22, 52, 93])

insert_index = np.searchsorted(sorted_arr, 21)

multiple_indexes = np.searchsorted(
    sorted_arr,
    [21, 52, 93]
)

print("\nInsertion index for 21:", insert_index)
print("Insertion indexes:", multiple_indexes)


# Sort numerical values
unsorted_arr = np.array([4, 93, 22, 21, 18, 19, 52])

print("\nSorted Numerical Array:")
print(np.sort(unsorted_arr))


# Sort strings alphabetically
fruit_arr = np.array(["banana", "cherry", "apple"])

print("\nSorted String Array:")
print(np.sort(fruit_arr))


# Sort Boolean values
boolean_arr = np.array([True, False, True])

print("\nSorted Boolean Array:")
print(np.sort(boolean_arr))


# Sort a 2-D array
two_dim_arr = np.array([
    [3, 2, 4],
    [5, 0, 1]
])

print("\nSorted 2-D Array:")
print(np.sort(two_dim_arr))


# Direct Boolean filtering
arr = np.array([41, 42, 43, 44])

boolean_filter = [True, False, True, False]
filtered_arr = arr[boolean_filter]

print("\nBoolean Filter Result:")
print(filtered_arr)


# Create a filter array using a loop
filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

filtered_values = arr[filter_arr]

print("\nGenerated Filter:", filter_arr)
print("Values greater than 42:", filtered_values)
