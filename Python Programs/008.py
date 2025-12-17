#Write a function to find squares of individual elements in a list using lambda function.

#1
# def squares(numlist):
#     return [num*num for num in numlist]

#2
# def squares(lam, nums):
#     return [lam(ele) for ele in nums]
# square = lambda a: a*a
# print(squares(square, [0, 1, 2, 3, 4, 5, 6]))

#3
squares = lambda numlist: [num*num for num in numlist]
print(squares([0,1,2,3,4,5,6]))