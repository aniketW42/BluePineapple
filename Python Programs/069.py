#Write a function to check whether a list contains the given sublist or not.

def is_sublist(li1, li2):

    while li2[0] in li1:
        idx = li1.index(li2[0])
        if li2 == li1[idx: idx + len(li2)]:
            return True
        else:
            li1 = li1[idx+1:]
    else:
        return False
    

print(is_sublist([1,2,3,4],[1,2,3]))
print(is_sublist([45,35,18,64, 96,13,75,42,31,2,64,6,5,46,95,23,46,15],[64,6,5,46]))