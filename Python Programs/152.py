# Write a function to sort the given array by using merge sort.

def merge_sort(arr: list)->list:

    n = len(arr)
    if n <= 1:
        return arr
    split1 = merge_sort(arr[:n//2])
    split2 = merge_sort(arr[n//2:])
    print("s1 ->",split1)
    print("s2 ->",split2)
    result = []
    idx1 = 0
    idx2 = 0
    

print(merge_sort([3,2,4,1,5]))