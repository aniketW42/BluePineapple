# Write a python function to find the sum of common divisors of two given numbers. 
def sumOfCommonDivisors(num1, num2):

    n = min(num1, num2)
    sum = 0
    for i in range(1, (n//2)+1):
        if num1%i == 0 and num2%i == 0:
            sum+= i

    if max(num1, num2)%n == 0:
        sum+=n

    return sum

print(sumOfCommonDivisors(6, 9))