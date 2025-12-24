#Write a python function to find the largest prime factor of a given number.

def largestPrimeFactor(num):
    divisors = [2,3,5,7,11]
    rem = num
    for divisor in divisors:
        while rem%divisor==0 and rem!=divisor:
            rem//=divisor
        
    return rem

print(largestPrimeFactor(13))