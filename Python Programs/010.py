#Write a function to get the n smallest items from a dataset.
import heapq
def nSmallest(dataset, n):
    heapq.heapify(dataset)
    result = []
    for _ in range(n):
        result.append(heapq.heappop(dataset))
    return result

print(nSmallest([4,2,5,3,7,1,6,8,9], 4))