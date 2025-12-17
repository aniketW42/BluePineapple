#Write a function to find sequences of lowercase letters joined with an underscore.
import re
def lowerLettersJoinedWithUnderscore(str):
    result = re.findall(r"[a-z]+_[a-z]+", str)
    return result

print(lowerLettersJoinedWithUnderscore("hehe_ha tyP_ol anik_Et Nor_maL"))