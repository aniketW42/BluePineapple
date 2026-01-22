"""
1. Array Basics + Types
    Create a 1D array of integers from 1 to 20.
    Print: shape , dtype , min , max , sum , mean .
    Convert it to float and show dtype change.

"""

import numpy as np 

integer_array = np.array(range(1, 21))

print(f"Shape :", integer_array.shape)
print(f"dtype :", integer_array.dtype)
print(f"min :", integer_array.min())
print(f"max :", integer_array.max())
print(f"sum :", integer_array.sum())
print(f"mean :", integer_array.mean())

float_array = integer_array.astype(float)
print("----------------------")
print(f"dtype (after converting to float) :", float_array.dtype)