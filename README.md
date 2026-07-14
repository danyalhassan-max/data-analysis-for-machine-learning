# ML Data Foundations

A structured learning repository focused on building numerical computing and data handling foundations for Machine Learning and Deep Learning.

This repository documents my practical learning through concept-based exercises, guided problem solving, and small projects.

## Repository Structure

```text
numpy/
├── 01_array_fundamentals.py
├── 02_indexing_and_slicing.py
├── 03_datatypes_copy_view.py
├── 04_shape_and_reshape.py
├── 05_iteration.py
├── 06_join_and_split.py
├── 07_search_sort_filter.py
├── 08_student_performance_analyzer.py
└── 09_random_and_distributions.py
```

## NumPy Topics Covered

### 01 — Array Fundamentals

* NumPy array creation
* 0D, 1D, 2D, and 3D arrays
* Array dimensions
* `ndim`

### 02 — Indexing and Slicing

* 1D, 2D, and 3D array indexing
* Array slicing
* Step slicing
* Row and column selection
* Multi-dimensional data access

### 03 — Data Types, Copy, and View

* NumPy data types
* Defining array data types
* Type conversion with `astype()`
* Copy vs view
* Array ownership with `base`

### 04 — Shape and Reshape

* Array shape
* Multi-dimensional shapes
* Reshaping arrays
* Converting between array structures

### 05 — Array Iteration

* Standard array iteration
* Nested iteration
* `nditer()`
* Buffered iteration
* `ndenumerate()`

### 06 — Join and Split

* `concatenate()`
* `stack()`
* `hstack()`
* `vstack()`
* `dstack()`
* `array_split()`
* Equal and unequal array splitting

### 07 — Search, Sort, and Filter

* `where()`
* Searching array values
* Odd and even value filtering
* `searchsorted()`
* Numerical and string sorting
* Boolean masking
* Array filtering

## 08 — Student Performance Analyzer

A NumPy mini project that applies core array operations to a structured 2D student marks dataset.

### Concepts Applied

* Representing a dataset using a 2D NumPy array
* Inspecting `ndim`, `shape`, `size`, and `dtype`
* Selecting samples and columns
* 2D array slicing
* Searching values with `where()`
* Boolean masking and filtering
* Sorting numerical values
* Protecting original data with `copy()`
* Reshaping 2D data into 1D
* Iterating through dataset values
* Splitting data into groups
* Rejoining arrays with `concatenate()`

### Dataset Structure Concept

```text
Rows    → Samples
Columns → Features
```

This structure is commonly used when representing numerical data for data analysis and Machine Learning workflows.

## 09 — Random Generation and Probability Distributions

### Random Generation

* Random integers
* Random floating-point values
* Random arrays
* Random sampling with `choice()`
* Weighted probability sampling
* Shuffle and permutation

### Probability Distributions

* Normal distribution
* Binomial distribution
* Poisson distribution
* Uniform distribution
* Logistic distribution
* Multinomial distribution
* Exponential distribution
* Chi-square distribution
* Rayleigh distribution
* Pareto distribution
* Zipf distribution

### Reproducibility

* Random seeds
* Reproducible random sequences
* NumPy `default_rng()`
* Independent random generators

### Distribution Visualization

Basic distribution visualization is used to inspect distribution shape and data concentration.

## Learning Goal

The goal of this repository is to develop practical foundations in:

* Numerical computing
* Array manipulation
* Numerical dataset handling
* Data preprocessing
* Reproducible experiments
* Machine Learning preparation
* Deep Learning preparation
* Image data processing foundations

The focus is on understanding concepts and applying them through code rather than only memorizing library syntax.

## Machine Learning Engineering Path

```text
Python Fundamentals
        ↓
Object-Oriented Programming
        ↓
NumPy
        ↓
Pandas
        ↓
Data Visualization
        ↓
Statistics for Machine Learning
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
Computer Vision
        ↓
Production ML Skills
```

## Career Focus

This repository is part of my Machine Learning Engineering learning path.

My focus is on developing practical skills in:

* Numerical computing
* Data preprocessing
* Exploratory data analysis
* Machine Learning
* Deep Learning
* Computer Vision
* Model training and evaluation
* Reproducible ML experiments
* Practical ML project development

These foundations will be applied across numerical data projects, Machine Learning applications, and Computer Vision projects.

## Current Status

* Python fundamentals — Completed
* Object-Oriented Programming — Completed
* NumPy core array operations — Completed
* NumPy mini project — Completed
* NumPy random generation and distributions — Completed
* NumPy universal functions (`ufunc`) — Next
* NumPy real dataset practice — Planned
* Pandas — Planned
* Data visualization — Planned
* Statistics for Machine Learning — Planned
* Machine Learning — Planned
* Deep Learning — Planned
