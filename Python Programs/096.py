#Write a python function to find the number of divisors of a given integer.

def number_of_divisors(num):
    if num == 0:
        return float('inf')
    
    num = abs(num)
    divisor_count = 0 

    i = 1
    while i*i <= num:
        if num%i == 0:
            divisor_count+= 1 if i*i == num else 2

        i+=1
    return divisor_count

# test
for i in range(-10, 20):
    print(f"Number of divisors of {i} -->", number_of_divisors(i))