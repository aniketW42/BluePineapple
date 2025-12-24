#Write a python function to convert a decimal number to binary number.

def dec_to_bin(num):
    if num == 0 : return 0
    binary = []
    while(num >= 1):
        binary.insert(0, str(num%2))
        num//=2
    return "".join(binary)

print(dec_to_bin(19))