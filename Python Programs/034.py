#Write a python function to find the missing number in a sorted array.

def find_missing(nums):
    s = 0
    e = len(nums) - 1

    while s <= e:
        mid = (s + e) // 2
        if nums[mid] == mid + 1:
            s = mid + 1
        else:
            e = mid - 1

    return s + 1

print(find_missing([2, 3, 4, 6, 7, 8, 9, 10]))

    