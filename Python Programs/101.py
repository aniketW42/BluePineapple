# Write a function to find the kth element in the given array.

def kth_element(array: list, k: int) -> int:
    if k > len(array) or k < 1:
        raise ValueError("Invalid index k")
    
    return array[k-1]

if __name__ == '__main__':
    print(kth_element([4,2,3,6,1,4,3], 1))
    print(kth_element([4,2,3,6,1,4,3], 2))
    print(kth_element([4,2,3,6,1,4,3], 3))
    print(kth_element([4,2,3,6,1,4,3], 7))
    # print(kth_element([4,2,3,6,1,4,3], 8)) #index out of bound
    # print(kth_element([4,2,3,6,1,4,3], -8)) #index out of bound and invalid k