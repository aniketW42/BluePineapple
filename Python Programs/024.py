#Write a function to convert the given binary number to its decimal equivalent.
import math
def binaryToDecimal(binary):
    binary = str(binary)
    decimal = 0
    for index, digit in enumerate(binary[::-1]):
        if digit == '1':
            decimal += math.pow(2, index)
    return int(decimal)

print(binaryToDecimal('10111'))