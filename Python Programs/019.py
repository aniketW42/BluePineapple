#Write a function to find whether a given array of integers contains any duplicate element.

def containDuplicate(nums):

    numset = set(nums)
    if len(nums) == len(numset):
        return False
    else:
        return True
    

if containDuplicate([1,2,3,4,5]):
    print("Contains duplicate element")
else:
    print("Does not contains duplicate element")
