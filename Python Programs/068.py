#Write a python function to check whether the given array is monotonic or not.

def is_monotonic1(arr):
    if not arr:
        return False

    sorted_arr = sorted(arr)
    if arr == sorted_arr or arr == sorted_arr[::-1]:
        return True
    else :
        return False

def is_monotonic2(arr):

    if not arr:
        return False

    prev = arr[0]

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

print(is_monotonic1([1,2,3,4,5]))
print(is_monotonic1([5,4,4,3]))
print(is_monotonic1([4,5,4,3,2]))
print(is_monotonic1([4,4,4,4]))
print(is_monotonic1([]))