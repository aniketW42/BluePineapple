#Write a python function to check whether the two numbers differ at one bit position only or not.

def is_one_bit_difference(num1, num2):
    flag = num1^num2
    if flag & (flag - 1) == 0:
        return True
    else:
        return False
    
print(is_one_bit_difference(12,14))