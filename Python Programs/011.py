#Write a python function to remove first and last occurrence of a given character from the string.

def removeFistAndLast(str, ch):
    if(ch not in str) : return str
    result = str.replace(ch,"",1)
    result = result[::-1].replace(ch,"", 1)[::-1]
    return result

print(removeFistAndLast("programming", "g"))


