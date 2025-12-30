#Write a function to split the given string with multiple delimiters by using regex.
import re
def split_with_muli_delimiters(string, delims):
    pattern = "|".join(map(re.escape, delims))
    return re.split(pattern, string)

print(split_with_muli_delimiters("this,is.an example!string;xyz",[",", " ", ".", "!", ";"] ))
