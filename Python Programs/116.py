# Write a function to convert a given tuple of positive integers into an integer.

def tuple_to_integer2(tup: tuple[int]) -> int:
    n = len(tup)-1
    result_num = 0
    for num in tup:
        result_num += int(10**n * num)
        n-=1
    return result_num

def tuple_to_integer1(tup: tuple[int]) -> int:
    int_str = "".join(str(num) for num in tup)
    return int(int_str)

if __name__ == '__main__':
    print(tuple_to_integer1((1,2,3,4)))
    print(tuple_to_integer2((1,2,3,4)))
    print(tuple_to_integer2((0,2,3,4)))
    print(tuple_to_integer2((0,2,3,0)))
    print(tuple_to_integer2((1,2,3,0)))
    print(tuple_to_integer2((0,0,0,0)))
    print(tuple_to_integer2((0,1,0,0)))
    print(tuple_to_integer2(()))

