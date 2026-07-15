"""
NumPy Universal Functions (ufunc)

Covers custom ufunc creation, arithmetic operations, rounding,
logarithms, aggregation, differences, number operations,
trigonometric functions, hyperbolic functions, and set operations.
"""

import numpy as np


# --------------------------------------------------
# Universal Function Introduction
# --------------------------------------------------

first_values = [1, 5, 3, 2, 7]
second_values = [3, 6, 4, 9, 5]

added_values = np.add(first_values, second_values)

print("Added values:", added_values)


# --------------------------------------------------
# Creating a Custom ufunc
# --------------------------------------------------

def add_values(first_value, second_value):
    return first_value + second_value


custom_add = np.frompyfunc(add_values, 2, 1)

custom_result = custom_add(
    [1, 4, 2, 7],
    [8, 5, 3, 6],
)

print("Custom ufunc result:", custom_result)
print("Custom function type:", type(custom_add))


# --------------------------------------------------
# Checking ufunc Type
# --------------------------------------------------

if isinstance(np.add, np.ufunc):
    print("np.add is a ufunc")
else:
    print("np.add is not a ufunc")


# --------------------------------------------------
# Simple Arithmetic
# --------------------------------------------------

first_array = np.array([21, 45, 32, 78, 54, 65])
second_array = np.array([34, 66, 43, 98, 23, 44])
negative_values = np.array([-22, 34, -25, -56])

addition = np.add(first_array, second_array)
subtraction = np.subtract(first_array, second_array)
multiplication = np.multiply(first_array, second_array)
division = np.divide(first_array, second_array)
remainder = np.mod(first_array, second_array)
division_remainder = np.divmod(first_array, second_array)
absolute_values = np.absolute(negative_values)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Remainder:", remainder)
print("Division and remainder:", division_remainder)
print("Absolute values:", absolute_values)


# Use smaller values to avoid integer overflow during power operations

power_bases = np.array([2, 3, 4, 5])
power_exponents = np.array([2, 3, 2, 3])

power_values = np.power(power_bases, power_exponents)

print("Power values:", power_values)


# --------------------------------------------------
# Rounding Decimals
# --------------------------------------------------

decimal_values = np.array([
    -22.00,
    34.342,
    -25.6756,
    -56.3423,
])

truncated_values = np.trunc(decimal_values)

print("Truncated values:", truncated_values)

rounded_value = np.around(3.4422, 2)
precise_rounded_value = np.around(3.657445444, 5)

print("Rounded to 2 decimals:", rounded_value)
print("Rounded to 5 decimals:", precise_rounded_value)

floor_values = np.floor([-3.7, 3.8])
ceil_values = np.ceil([-3.7, 3.8])

print("Floor values:", floor_values)
print("Ceil values:", ceil_values)


# --------------------------------------------------
# Logarithmic Functions
# --------------------------------------------------

log_values = np.arange(1, 10)

print("Base-2 logarithm:", np.log2(log_values))
print("Base-10 logarithm:", np.log10(log_values))
print("Natural logarithm:", np.log(log_values))


# --------------------------------------------------
# Summations
# --------------------------------------------------

first_array = np.array([21, 45, 32, 78, 54, 65])
second_array = np.array([34, 66, 43, 98, 23, 44])

elementwise_sum = np.add(first_array, second_array)
total_sum = np.sum([first_array, second_array])
row_sums = np.sum([first_array, second_array], axis=1)
cumulative_sum = np.cumsum(first_array)

print("Element-wise sum:", elementwise_sum)
print("Total sum:", total_sum)
print("Sum of each array:", row_sums)
print("Cumulative sum:", cumulative_sum)


# --------------------------------------------------
# Products
# --------------------------------------------------

first_product_array = np.array([1, 4, 3, 5])
second_product_array = np.array([1, 2, 9, 5])

array_product = np.prod(first_product_array)

combined_product = np.prod([
    first_product_array,
    second_product_array,
])

row_products = np.prod(
    [first_product_array, second_product_array],
    axis=1,
)

cumulative_product = np.cumprod(first_product_array)

print("Array product:", array_product)
print("Combined product:", combined_product)
print("Product of each array:", row_products)
print("Cumulative product:", cumulative_product)


# --------------------------------------------------
# Differences
# --------------------------------------------------

first_difference = np.diff(first_product_array)

array_differences = np.diff([
    first_product_array,
    second_product_array,
])

second_difference = np.diff(
    first_product_array,
    n=2,
)

print("First difference:", first_difference)
print("Array differences:", array_differences)
print("Second difference:", second_difference)


# --------------------------------------------------
# Least Common Multiple
# --------------------------------------------------

first_number = 10
second_number = 26

least_common_multiple = np.lcm(
    first_number,
    second_number,
)

lcm_values = np.array([3, 6, 9])

array_lcm = np.lcm.reduce(lcm_values)

range_values = np.arange(1, 11)
range_lcm = np.lcm.reduce(range_values)

print("LCM:", least_common_multiple)
print("Array LCM:", array_lcm)
print("Range LCM:", range_lcm)


# --------------------------------------------------
# Greatest Common Divisor
# --------------------------------------------------

greatest_common_divisor = np.gcd(
    first_number,
    second_number,
)

gcd_values = np.array([3, 6, 9])

array_gcd = np.gcd.reduce(gcd_values)
range_gcd = np.gcd.reduce(range_values)

print("GCD:", greatest_common_divisor)
print("Array GCD:", array_gcd)
print("Range GCD:", range_gcd)


# --------------------------------------------------
# Trigonometric Functions
# --------------------------------------------------

angle_radians = np.array([
    np.pi / 2,
    np.pi / 3,
    np.pi / 4,
    np.pi / 5,
])

sine_values = np.sin(angle_radians)
angles_degrees = np.rad2deg(angle_radians)

print("Sine values:", sine_values)
print("Radians to degrees:", angles_degrees)

degree_values = np.array([90, 180, 270, 360])

angles_radians = np.deg2rad(degree_values)

print("Degrees to radians:", angles_radians)


# --------------------------------------------------
# Inverse Trigonometric Functions
# --------------------------------------------------

inverse_sine = np.arcsin(1.0)
inverse_cosine = np.arccos(1.0)

inverse_values = np.array([-1, 0, 0.1])

inverse_sine_values = np.arcsin(inverse_values)
inverse_tangent_values = np.arctan(inverse_values)

print("Inverse sine:", inverse_sine)
print("Inverse cosine:", inverse_cosine)
print("Inverse sine values:", inverse_sine_values)
print("Inverse tangent values:", inverse_tangent_values)


# --------------------------------------------------
# Hyperbolic Functions
# --------------------------------------------------

hyperbolic_input = np.array([1, 2, 3])

hyperbolic_sine = np.sinh(hyperbolic_input)
inverse_hyperbolic_cosine = np.arccosh(hyperbolic_input)

print("Hyperbolic sine:", hyperbolic_sine)
print(
    "Inverse hyperbolic cosine:",
    inverse_hyperbolic_cosine,
)


# --------------------------------------------------
# Hypotenuse
# --------------------------------------------------

base = 4
perpendicular = 3

hypotenuse = np.hypot(base, perpendicular)

print("Hypotenuse:", hypotenuse)


# --------------------------------------------------
# Set Operations
# --------------------------------------------------

duplicate_values = np.array([
    1, 1, 1, 2, 3, 4, 5, 5, 6, 7
])

unique_values = np.unique(duplicate_values)

print("Unique values:", unique_values)

first_set = np.array([1, 2, 7, 4])
second_set = np.array([3, 4, 5, 6])

union_values = np.union1d(first_set, second_set)

intersection_values = np.intersect1d(
    first_set,
    second_set,
    assume_unique=True,
)

difference_values = np.setdiff1d(
    first_set,
    second_set,
    assume_unique=True,
)

symmetric_difference = np.setxor1d(
    first_set,
    second_set,
    assume_unique=True,
)

print("Union:", union_values)
print("Intersection:", intersection_values)
print("Difference:", difference_values)
print("Symmetric difference:", symmetric_difference)
