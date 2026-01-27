# Write a function to find the ascii value of total characters in a string.

def ascii_of_all_ele_in_string(string: str) -> int:
    """
    Return total of ascii values
    """
    total = 0
    for char in string:
        total += ord(char)

    return total

if __name__ == "__main__":
    print(ascii_of_all_ele_in_string("test"))
    print(ascii_of_all_ele_in_string("1234"))
    print(ascii_of_all_ele_in_string("abcd"))