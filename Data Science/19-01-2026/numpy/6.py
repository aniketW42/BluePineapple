"""
6. Fancy Indexing + Scatter Update
    Create a length-30 zero array.
    Randomly pick 8 unique positions and set them to 1.
    Then set positions divisible by 5 to 9 (overwriting if needed).

"""

import numpy as np

# creating zeros array
zero_array = np.zeros(30, dtype=int)
print(zero_array)

# Randomly pick 8 unique positions and set them to 1
random_indices = np.random.randint(0, 30, 8)
zero_array[random_indices] = 1
print(zero_array)

#set positions divisible by 5 to 9
positions_divisible_by_five = [idx for idx in range(0, 30) if idx%5==0]
zero_array[positions_divisible_by_five] = 9
print(zero_array)

