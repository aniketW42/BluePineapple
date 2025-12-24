# Write a function to filter even numbers using lambda function.

def filter_even(li):
    isEven = lambda x : x % 2 == 0  
    return [ele for ele in li if isEven(ele)]

print(filter_even([1,2,3,4,5,6,7,8,9,10]))