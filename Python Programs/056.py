#Write a python function to check if a given number is one less than twice its reverse.

def reverse(num):
    if num == 0: return 0
    n = abs(num)
    rev = 0
    while n>0:
        rem = n%10
        rev = rev*10 + rem
        n = n//10
    return rev * num // abs(num)

def is_one_less_than_twice_its_reverce(num):
    return num == (2*reverse(num)) - 1

print(is_one_less_than_twice_its_reverce(73))
print(is_one_less_than_twice_its_reverce(12))
print(is_one_less_than_twice_its_reverce(1))
print(is_one_less_than_twice_its_reverce(0))
print(is_one_less_than_twice_its_reverce(-72))

