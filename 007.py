#Write a function to find all words which are at least 4 characters long in a string by using regex.
import re
def findWords(str):
    words4char = re.findall(r"\b\w{4,4}\b", str)
    return words4char

print(findWords("this is an sample string, find four char "))
