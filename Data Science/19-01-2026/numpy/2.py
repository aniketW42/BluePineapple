"""
2. Slicing + Boolean Masking
    Create an array of 50 random integers between 1 and 100.
    Extract:
        all even numbers
        numbers divisible by 3 and > 50
    Replace values < 20 with 20 (without loops).

"""
import numpy as np

# creating numpy array of random 50 numbers from  1-100
integers = np.array(np.random.randint(1, 100, 50))

# extract all even numbers
all_even = integers[integers % 2 == 0]

# extract all numbers divisible by 3 and > 50
divisible_by_three_and_gt_fifty = integers[(integers % 3 == 0) & (integers > 50)]

print("All even numbers:\n", all_even)
print("-------------------------------------------------------------------------")

print("Numbers divisible by 3 and > 50:\n", divisible_by_three_and_gt_fifty)
print("-------------------------------------------------------------------------")

# Replace values < 20 with 20 
integers[integers < 20] = 20

print("After replacing values<20 with 20:\n", integers)