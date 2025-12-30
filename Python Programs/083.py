#Write a python function to find the character made by adding all the characters of the given string.

def add_chars_get_char(string):
    sum = 0
    for char in string:
        char = char.lower()
        sum += ord(char) - 96

    return chr(sum%26 + 96)


print(add_chars_get_char("aaa"))
print(add_chars_get_char("a"))
print(add_chars_get_char("abcde"))

