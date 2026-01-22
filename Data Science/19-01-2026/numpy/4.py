"""
4. Broadcasting Practice
    Create a (4, 5) matrix of random floats.
    Create a (5,) vector and add it to every row using broadcasting.
    Normalize each row to sum to 1 (handle division carefully).

"""

import numpy as np

#Create a (4, 5) matrix of random floats.
matrix = np.array(np.random.rand(4, 5))
print("(4, 5) matrix:\n", matrix)

#Create a (5,) vector and add it to every row using broadcasting.
vector = np.array(np.random.rand(5))
brd_sum = matrix + vector
print("\nAfter adding vector:\n", brd_sum)
#Normalize each row to sum to 1 (handled division using keepdims=true)
row_sum = brd_sum.sum(axis=1, keepdims=True)
normalized_brd_sum = brd_sum / row_sum

print("\nAfter normalization:\n", normalized_brd_sum)
