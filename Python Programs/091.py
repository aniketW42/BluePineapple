#Write a function to check if a substring is present in a given list of string values.

def is_substring_present(strings, substring):

    if not strings:
        return False
    
    for string in strings:
        if substring in string:
            return True
    
    return False
        

print(is_substring_present(["India", "Japan", "Nepal", "Bhutan"], "dia"))
print(is_substring_present(["India", "Japan", "Nepal", "Bhutan"], "nadia"))