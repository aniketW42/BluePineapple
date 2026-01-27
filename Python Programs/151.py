# Write a python function to check whether the given number is co-prime or not.



def is_coprime(num1, num2) -> bool:

    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1==1

print(is_coprime(2, 9))
print(is_coprime(3, 9))
print(is_coprime(9, 2))