#Write a python function to check whether the length of the word is odd or not.

def is_lenOdd(word):
    return len(word.strip())%2 == 1

print(is_lenOdd("wher"))