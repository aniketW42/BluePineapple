#Write a python function to find the sum of repeated elements in a given array.

from collections import Counter

def sum_of_repeated(li):
    freq = Counter(li)
    sum = 0
    for key, val in freq.items():
        if val > 1:
            sum+= key*val

    return sum

print(sum_of_repeated([1,2,3,4,4,5,5,6]))

