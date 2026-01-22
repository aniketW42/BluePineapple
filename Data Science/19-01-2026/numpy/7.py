"""
7. Sorting + Top-K Without Full Sort
    Create 100 random numbers (floats).
    Find top 10 values and their indices using an efficient approach
    (argpartition).
    Print top 10 sorted descending (values + indices aligned).

"""
import numpy as np

# creating random 100 numbers
numbers = np.array(np.random.rand(100))

# index of top 10 elements
top_idx = np.argpartition(numbers, -10)[-10:][::-1]

# top 10 elements
top_vals = numbers[top_idx]

# top 10 sorted descending (values + indices aligned)
top_idx_and_vals = np.array([top_idx, top_vals]).T

print("-->\n",top_idx_and_vals )
