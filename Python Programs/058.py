#Write a python function to check whether the given two integers have opposite sign or not.

def has_oppo_sign(num1, num2):
    return (num1 * num2) == (abs(num1)*abs(num2))

print(has_oppo_sign(1, 2))
print(has_oppo_sign(-3, 2))
print(has_oppo_sign(3, -2))
print(has_oppo_sign(-3, -2))