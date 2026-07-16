"""
Student Score Analyzer using NumPy

Features:
- Load CSV dataset
- Explore dataset information
- Calculate descriptive statistics
- Filter high-performing students
- Calculate per-student averages
- Normalize data
- Perform Min-Max Scaling
- Save normalized dataset

Author: Your Name
"""

import numpy as np


# ==========================================
# Load Dataset
# ==========================================

student_scores = np.loadtxt(
    "datasets/student_scores.csv",
    delimiter=",",
    skiprows=1
)


# ==========================================
# Dataset Information
# ==========================================

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print(f"Dimensions : {student_scores.ndim}")
print(f"Shape      : {student_scores.shape}")
print(f"Size       : {student_scores.size}")
print(f"Data Type  : {student_scores.dtype}")


# ==========================================
# Extract Subject Scores
# ==========================================

math_scores = student_scores[:, 0]
reading_scores = student_scores[:, 1]
writing_scores = student_scores[:, 2]


# ==========================================
# Subject Statistics
# ==========================================

print("\n========== MATH ==========")
print("Average :", np.mean(math_scores))
print("Std Dev :", np.std(math_scores))
print("Maximum :", np.max(math_scores))
print("Minimum :", np.min(math_scores))

print("\n========== READING ==========")
print("Average :", np.mean(reading_scores))
print("Std Dev :", np.std(reading_scores))
print("Maximum :", np.max(reading_scores))
print("Minimum :", np.min(reading_scores))

print("\n========== WRITING ==========")
print("Average :", np.mean(writing_scores))
print("Std Dev :", np.std(writing_scores))
print("Maximum :", np.max(writing_scores))
print("Minimum :", np.min(writing_scores))


# ==========================================
# Overall Dataset Statistics
# ==========================================

print("\n========== OVERALL ==========")
print("Overall Average :", np.mean(student_scores))
print("Overall Std Dev :", np.std(student_scores))


# ==========================================
# Boolean Masking
# ==========================================

high_math_scores = math_scores[math_scores > 80]

print("\nStudents Scoring Above 80 in Math")
print(high_math_scores)


# ==========================================
# Average Score Per Student
# ==========================================

student_average = np.mean(student_scores, axis=1)

print("\nAverage Score of Each Student")
print(student_average)


# ==========================================
# Normalization (0-1)
# ==========================================

normalized_scores = student_scores / 100

print("\nNormalized Scores")
print(normalized_scores)


# ==========================================
# Save Normalized Dataset
# ==========================================

np.savetxt(
    "datasets/normalized_student_scores.csv",
    normalized_scores,
    delimiter=",",
    fmt="%.2f"
)


# ==========================================
# Min-Max Scaling
# ==========================================

math_min = np.min(math_scores)
math_max = np.max(math_scores)

math_minmax = (math_scores - math_min) / (math_max - math_min)

print("\nMath Scores After Min-Max Scaling")
print(math_minmax)


print("\nProject Completed Successfully!")
