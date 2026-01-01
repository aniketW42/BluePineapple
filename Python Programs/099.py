# Write a function to convert the given decimal number to its binary equivalent.

# solution 1
def decimal_to_binary1(decimal: int) -> str:
    if decimal == 0:
        return '0b0'

    binary = ''
    while decimal >= 1:
        rem = int(decimal % 2)
        binary =  str(rem) + binary
        decimal //= 2
    
    return '0b' + binary

# solution 2 (efficient for larger numbers)
def decimal_to_binary2(decimal: int) -> str:
    if decimal == 0:
        return '0b0'

    binary = ''
    while decimal >= 1:
        rem = decimal & 1 
        binary =  str(rem) + binary
        decimal = decimal >> 1
    
    return '0b' + binary


if __name__ == "__main__":
    print(decimal_to_binary2(8))
    print(decimal_to_binary2(9))
    print(decimal_to_binary2(12))
    print(decimal_to_binary2(0))