# Write a function to sort the given array by using counting sort.

def counting_sort(arr):
    #1) find max
    max_ele = max(arr)
    #2) create array of max+1 elements initialized by zero
    count_arr = [0 for _ in range(max_ele+1)]
    #3) calculate count of each ele
    for ele in arr:
        count_arr[ele] += 1
    #4) calculate cummulative sum
    for i in range(1,len(count_arr)):
        count_arr[i] = count_arr[i-1] + count_arr[i]
    #5) it is what it is
    sorted_arr = [0 for _ in range(len(arr))]
    for ele in arr:
        count_arr[ele] = count_arr[ele] - 1
        sorted_arr[count_arr[ele]] = ele
    
    return sorted_arr




print(counting_sort([2,4,4,6,2,8]))
