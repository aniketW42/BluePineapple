#Write a function to find the first duplicate element in a given array of integers.

def firstDuplicate(nums):
    for i in range(len(nums)):
        temp = nums[:i] + nums[i+1:]
        if(nums[i] in temp):
            return nums[i]
        
    return None
    

print(firstDuplicate([1,2,3,4,5,6,7]))