#Write a python function to find smallest number in a list.

def smallest(li):
    if li:
        mini = li[0]
    else:
        return None
    
    for ele in li:
        if ele < mini:
            mini = ele

    return mini


print(smallest([1,2,3,-2,5,-7,8,0]))
print(smallest([86,45,24,78,35]))
print(smallest([-45,-2,-71,-34,-56,-7,-56]))
print(smallest([2,2,5,5,-1,-1,0,0,68,68]))
print(smallest([]))