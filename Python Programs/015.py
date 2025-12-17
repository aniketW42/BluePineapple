#Write a function to split a string at lowercase letters.
import re
def splitAtLower(str):
    result = re.split(r"[a-z]+", str)
    if result[-1] == "" : 
        del result[-1]
    return result

print(splitAtLower("THISabcISnAxyzSTRINGhkk HElLO WoRLd"))