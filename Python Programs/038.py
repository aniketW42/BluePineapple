#Write a function to find the division of first even and odd number of a given list.

def first_evenodd_div(li):
    even = None
    odd = None
    for ele in li:
        if not even and ele%2==0:
            even = ele
        elif not odd and ele%2==1:
            odd = ele
        if even and odd:
            break

    if not even or not odd:
        return None
    
    return even/odd

print(first_evenodd_div([2,6,4,6,4,1]))