#Write a python function to find the length of the longest word.

def len_of_longest_word(string):
    
    string = string.strip()
    strings = string.split(" ")

    maxstr = max(strings, key = len)

    return len(maxstr)

print(len_of_longest_word("Program number ninety"))