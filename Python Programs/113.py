# Write a function to check if a string represents an integer or not.
import re

def is_integer_string(string: str) -> bool:
    str_new = bool(re.fullmatch(r"0|[+-]?\d+", string))
    return str_new


if __name__ == "__main__":
    print(is_integer_string("1234"))  # True
    print(is_integer_string("1234u"))  # False
    print(is_integer_string("-7"))  # True
    print(is_integer_string("3.14"))  # False
    print(is_integer_string("01"))  # True
    # can use "0|[+-]?\d+" if leading zeros are not allowed
    print(is_integer_string(""))  # False
