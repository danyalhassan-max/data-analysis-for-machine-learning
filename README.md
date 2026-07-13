# NumPy Learning and Practice

A structured NumPy learning repository focused on building strong
numerical computing foundations for Machine Learning and Deep Learning.

The repository contains concept-based practice files and a mini project
that applies core NumPy operations to a simple dataset.

## Repository Structure

``` text
numpy/
├── 01_array_fundamentals.py
├── 02_indexing_and_slicing.py
├── 03_datatypes_copy_view.py
├── 04_shape_and_reshape.py
├── 05_iteration.py
├── 06_join_and_split.py
├── 07_search_sort_filter.py
└── projects/
    └── student_performance_analyzer.py
```

## Topics Covered

### 01 --- Array Fundamentals

-   NumPy array creation
-   0D, 1D, 2D, and 3D arrays
-   Array dimensions
-   `ndim`

### 02 --- Indexing and Slicing

-   1D array indexing
-   2D array indexing
-   3D array indexing
-   Array slicing
-   Step slicing
-   Row and column selection

### 03 --- Data Types, Copy, and View

-   NumPy data types
-   Defining array data types
-   Type conversion with `astype()`
-   Copy vs view
-   Understanding array ownership with `base`

### 04 --- Shape and Reshape

-   Array shape
-   Multi-dimensional shapes
-   Reshaping arrays
-   Converting between array structures

### 05 --- Array Iteration

-   Standard array iteration
-   Nested iteration
-   `nditer()`
-   Buffered iteration
-   `ndenumerate()`

### 06 --- Join and Split

-   `concatenate()`
-   `stack()`
-   `hstack()`
-   `vstack()`
-   `dstack()`
-   `array_split()`

### 07 --- Search, Sort, and Filter

-   `where()`
-   Odd and even value searching
-   `searchsorted()`
-   Numeric sorting
-   String sorting
-   Boolean sorting
-   Boolean filtering

## Mini Project --- Student Performance Analyzer

The Student Performance Analyzer applies NumPy fundamentals to a 2D
student marks dataset.

### Concepts Applied

-   Dataset representation using a 2D array
-   Dataset inspection with `ndim`, `shape`, `size`, and `dtype`
-   Row and column selection
-   2D slicing
-   Searching values with `where()`
-   Boolean masking and filtering
-   Sorting student marks
-   Protecting original data with `copy()`
-   Reshaping 2D data into 1D
-   Iterating with `nditer()`
-   Splitting data into groups
-   Rejoining datasets with `concatenate()`

### Machine Learning Connection

The project introduces an important data representation pattern:

``` text
Rows    → Samples
Columns → Features
```

This same structure is commonly used when preparing datasets for Machine
Learning.

## Learning Goal

The goal of this repository is not only to practice NumPy syntax. It is
to build the array manipulation and data handling skills required for:

-   Data preprocessing
-   Machine Learning
-   Deep Learning
-   Image data processing
-   CNN-based projects

Goal
↓
Machine Learning Engineering foundations

Python
↓
NumPy
↓
Pandas
↓
Data Visualization
↓
Machine Learning
↓
Deep Learning
↓
Computer Vision
↓
Production ML skills

## Career Focus

This repository is part of my Machine Learning Engineering learning path.

My focus is on developing practical skills in:

- Numerical computing
- Data preprocessing
- Exploratory data analysis
- Machine Learning
- Deep Learning
- Computer Vision
- Model training and evaluation
- Reproducible ML experiments

These foundations will be applied to multiple practical projects, including computer vision and medical image classification.

## Status

NumPy core array operations completed. Random distributions, universal
functions, and ML-focused NumPy practice are the next learning stages.
