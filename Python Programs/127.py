# Write a function to multiply two integers without using the * operator in python.


def multiplyWithoutStartOperator(num1, num2):
    is_negative = False

    if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
        is_negative = True

    num1, num2 = abs(num1), abs(num2)
    mult = 0
    for _ in range(num2):
        mult += num1

    return -mult if is_negative else mult


print(multiplyWithoutStartOperator(2, 2))
print(multiplyWithoutStartOperator(2, 4))
print(multiplyWithoutStartOperator(3, 10))
print(multiplyWithoutStartOperator(-3, 10))
print(multiplyWithoutStartOperator(-3, -10))
print(multiplyWithoutStartOperator(3, -10))
