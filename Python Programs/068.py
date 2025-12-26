#Write a python function to check whether the given array is monotonic or not.

# def is_monotonic(arr):
#     if arr == sorted(arr) or arr == sorted(arr , reverse=True):
#         return True
#     else :
#         return False

def is_monotonic(arr):
    
    if arr:
        prev = arr[0]
    else : return None
    inc = True
    dec = True
    for ele in arr:
        if inc and ele>prev:
            dec = False
        elif dec and ele<prev:
            inc = False
        elif ele==prev:
            pass
        else:
            return False
        prev = ele
    return True



print(is_monotonic([1,2,3,4,5]))
print(is_monotonic([5,4,4,3]))
print(is_monotonic([4,5,4,3,2]))
print(is_monotonic([4]))
print(is_monotonic([]))