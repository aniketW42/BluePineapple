"""
Reshape + Axis Operations
    Create an array from 1 to 60 and reshape into (5, 12).
    Compute:
        row-wise sums
        column-wise means
        global std
    Find the index of the maximum value in the 2D array.

"""

import numpy as np

arr = np.array(range(1, 61)).reshape(5, 12)

row_wise_sums = arr.sum(axis=1)

column_wise_means = arr.mean(axis=0)

global_std = arr.std()

print("row-wise sums:", row_wise_sums)
print("\ncolumn-wise means:", column_wise_means)
print("\nglobal std:", global_std)

row_index = arr.argmax(axis=0)[0]
col_index = arr.argmax(axis=1)[0]

max_index = (row_index, col_index)
print("\nIndex of the maximum value in the 2D array:", max_index)