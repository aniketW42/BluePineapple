#Write a python function to find the maximum sum of elements of list in a list of lists.

def maxSum(lists):
    max = sum(lists[0])
    for list in lists:
        s = sum(list)
        if max < s : max =s
    return max

print(maxSum([[1,2,3],[1,2],[1,2,4],[6,2,4]]))