#Write a python function to find the product of non-repeated elements in a given array.
import math
def productOfNonRepeated(nums):
    if not nums:
        return 0
    repeated = set()
    unique = set()
    for num in nums:
        if num in unique:
            repeated.add(num)
        else:
            unique.add(num)

    if(0 in unique and 0 in repeated):
        unique.remove(0)
        repeated.remove(0)

    result = math.prod(unique) / math.prod(repeated)
    return result

print(productOfNonRepeated([-2,-2,-3,5]))
    