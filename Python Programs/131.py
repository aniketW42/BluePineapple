# Write a python function to reverse only the vowels of a given string.

def reverce_vowels_only(string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])

    chars = list(string)

    start = 0
    end = len(string) - 1

    while start < end :

        s_is_vowel = chars[start].lower() in vowels
        e_is_vowel = chars[end].lower() in vowels

        if not s_is_vowel:
            start+=1
        if not e_is_vowel:
            end-=1
        
        if s_is_vowel and e_is_vowel:
            chars[start], chars[end] = chars[end], chars[start]
            start+=1
            end-=1

    return "".join(chars)  

print(reverce_vowels_only("Hello world"))
print(reverce_vowels_only("HEllO wOrld"))

