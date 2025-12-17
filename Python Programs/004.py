import heapq

def findLargest(nums):
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)
    print(-max_heap[0])

    
#another approach
# def findLargest(nums):
#     max_heap = []
#     for num in nums:
#         heapq.heappush(max_heap, -num)
#     print(f"The largest number is {-max_heap[0]}")

findLargest([47, 12, 89, 5, 63, 74, 31, 8, 57, 20])