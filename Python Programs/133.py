# Write a function to calculate the sum of the negative numbers of a given list of numbers using lambda function.

def sum_of_negative(numbers):

    negative_nums = list(filter(lambda num: num<0, numbers))
    return sum(negative_nums)

print(sum_of_negative([1,2,3,-4,-5]))
print(sum_of_negative([]))