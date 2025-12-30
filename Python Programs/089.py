#Write a function to find the closest smaller number than n.

def closest_smaller(li, n):
    closest = None
    for ele in li:
        if not closest and ele < n:
            closest = ele
        elif ele < n and n-ele < n-closest:
            closest = ele
    
    return closest

print(closest_smaller([55,43,51,63,66,51,46,66,11,66,44], 66))
print(closest_smaller([55,43,51,63,66,51,46,66,11,66,44], 11))
