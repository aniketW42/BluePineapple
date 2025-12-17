#Write a function to remove characters from the first string which are present in the second string.
def removeCommonChar(str1, str2):
    newstr = ""
    for char in str1:
        if char not in str2:
            newstr = newstr + char

    return newstr

print(removeCommonChar("hello world", "lr"))