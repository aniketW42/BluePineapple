#Write a python function to remove all digits from a list of strings.
import re
def removeDig(strings):
    digremoved = []
    for str in strings:
        digremoved.append(re.sub(r"\d+", "", str))
    return digremoved

print(removeDig(["hello123", "123hello", "he123llo"]))