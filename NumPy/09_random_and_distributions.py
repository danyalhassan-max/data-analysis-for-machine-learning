"""
NumPy Random and Probability Distributions

Covers random number generation, sampling, permutations,
probability distributions, reproducibility, and NumPy's
modern random Generator API.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# Random Integers and Floats
# --------------------------------------------------

random_int = np.random.randint(100)
print("Random integer:", random_int)

random_float = np.random.rand()
print("Random float:", random_float)

random_matrix = np.random.rand(2, 4)
print("Random 2D array:\n", random_matrix)


# --------------------------------------------------
# Random Arrays
# --------------------------------------------------

one_dimensional = np.random.randint(100, size=5)
print("1D random array:", one_dimensional)

two_dimensional = np.random.randint(100, size=(4, 5))
print("2D random array:\n", two_dimensional)


# --------------------------------------------------
# Random Choice and Probability
# --------------------------------------------------

random_value = np.random.choice([2, 3, 6, 4, 8])
print("Random choice:", random_value)

random_choices = np.random.choice(
    [1, 3, 6, 9, 4, 2],
    size=(3, 5),
)
print("Random choices:\n", random_choices)

weighted_choices = np.random.choice(
    [3, 5, 7, 9],
    p=[0.1, 0.3, 0.6, 0.0],
    size=(3, 4),
)
print("Weighted random choices:\n", weighted_choices)


# --------------------------------------------------
# Shuffle and Permutation
# --------------------------------------------------

shuffle_array = np.array([2, 6, 4, 8, 1])
np.random.shuffle(shuffle_array)

print("Shuffled array:", shuffle_array)

permutation_array = np.array([2, 7, 4, 9])

print(
    "Permutation:",
    np.random.permutation(permutation_array),
)

print(
    "Original array after permutation:",
    permutation_array,
)


# --------------------------------------------------
# Normal Distribution
# --------------------------------------------------

normal_values = np.random.normal(
    loc=6,
    scale=2,
    size=(2, 3),
)

print("Normal distribution:\n", normal_values)

sns.displot(
    np.random.normal(loc=3, scale=1, size=1000),
    kind="kde",
)

plt.show()


# --------------------------------------------------
# Binomial Distribution
# --------------------------------------------------

binomial_values = np.random.binomial(
    n=10,
    p=0.5,
    size=10,
)

print("Binomial distribution:", binomial_values)

sns.displot(
    np.random.binomial(
        n=20,
        p=0.6,
        size=1000,
    )
)

plt.show()


# --------------------------------------------------
# Normal vs Binomial Distribution
# --------------------------------------------------

distribution_data = {
    "normal": np.random.normal(
        loc=50,
        scale=5,
        size=1000,
    ),
    "binomial": np.random.binomial(
        n=100,
        p=0.5,
        size=1000,
    ),
}

sns.displot(distribution_data, kind="kde")

plt.show()


# --------------------------------------------------
# Poisson Distribution
# --------------------------------------------------

poisson_values = np.random.poisson(
    lam=7,
    size=10,
)

print("Poisson distribution:", poisson_values)

sns.displot(
    np.random.poisson(lam=2, size=1000)
)

plt.show()


# --------------------------------------------------
# Uniform Distribution
# --------------------------------------------------

uniform_values = np.random.uniform(
    low=2,
    high=10,
    size=13,
)

print("Uniform distribution:", uniform_values)

sns.displot(
    np.random.uniform(
        low=2,
        high=10,
        size=1000,
    ),
    kind="kde",
)

plt.show()


# --------------------------------------------------
# Logistic Distribution
# --------------------------------------------------

logistic_values = np.random.logistic(
    loc=1,
    scale=2,
    size=5,
)

print("Logistic distribution:", logistic_values)

sns.displot(
    np.random.logistic(size=1000),
    kind="kde",
)

plt.show()


# --------------------------------------------------
# Multinomial Distribution
# --------------------------------------------------

dice_results = np.random.multinomial(
    n=6,
    pvals=[
        1 / 6,
        1 / 6,
        1 / 6,
        1 / 6,
        1 / 6,
        1 / 6,
    ],
)

print("Multinomial dice results:", dice_results)

category_results = np.random.multinomial(
    n=200,
    pvals=[0.7, 0.2, 0.1],
)

print("Simulated category counts:", category_results)


# --------------------------------------------------
# Exponential Distribution
# --------------------------------------------------

waiting_times = np.random.exponential(
    scale=365,
    size=10,
)

print("Simulated waiting times:", waiting_times)

sns.displot(
    np.random.exponential(
        scale=365,
        size=1000,
    ),
    kind="kde",
)

plt.show()


# --------------------------------------------------
# Chi-Square Distribution
# --------------------------------------------------

chi_square_values = np.random.chisquare(
    df=2,
    size=2,
)

print("Chi-square distribution:", chi_square_values)

sns.displot(
    np.random.chisquare(
        df=1,
        size=1000,
    ),
    kind="kde",
)

plt.show()


# --------------------------------------------------
# Rayleigh Distribution
# --------------------------------------------------

rayleigh_values = np.random.rayleigh(
    scale=5,
    size=(2, 3),
)

print("Rayleigh distribution:\n", rayleigh_values)

sns.displot(
    np.random.rayleigh(
        scale=3,
        size=1000,
    )
)

plt.show()


# --------------------------------------------------
# Pareto Distribution
# --------------------------------------------------

pareto_values = np.random.pareto(
    a=2,
    size=(2, 3),
)

print("Pareto distribution:\n", pareto_values)

sns.displot(
    np.random.pareto(
        a=2,
        size=1000,
    )
)

plt.show()


# --------------------------------------------------
# Zipf Distribution
# --------------------------------------------------

zipf_values = np.random.zipf(
    a=2,
    size=(2, 3),
)

print("Zipf distribution:\n", zipf_values)

sns.displot(
    np.random.zipf(
        a=2,
        size=1000,
    )
)

plt.show()


# --------------------------------------------------
# Random Seed and Reproducibility
# --------------------------------------------------

np.random.seed(10)

seeded_value = np.random.random()

print("Seeded random value:", seeded_value)


# --------------------------------------------------
# Modern NumPy Generator API
# --------------------------------------------------

rng = np.random.default_rng(10)
rng_second = np.random.default_rng(20)

print("Generator with seed 10:", rng.random())
print("Generator with seed 20:", rng_second.random())
