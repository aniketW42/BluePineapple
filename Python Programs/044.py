#Write a function that matches a word at the beginning of a string.
import re
def is_matching(string, word):
    if re.match(r"\A" + word, string):
        return True
    else:
        return False
         
print(is_matching("is this is string", "this"))
