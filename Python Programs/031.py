# Write a function to find the top k integers that occur most frequently from given lists of sorted and distinct integers using 
# heap queue algorithm.
import heapq
from collections import Counter
def topK(lists, k):
    merged = heapq.merge(*lists)
    freq = Counter(merged)
    sortedfreq = sorted(freq.items(), key = lambda x:x[1], reverse=True)
    return [tup[0] for tup in sortedfreq[0:k] ]
    

input = [
    [2,4,5,9],
    [1,3,5,8],
    [6,8,9,8],
    [5,6,7,10]
]

print(topK(input,5))

