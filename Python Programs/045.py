#Write a function to find the gcd of the given array elements.

def gcd_of_arry(li):
    for i in range(min(li), 1, -1):
        if all(ele%i == 0 for ele in li):
            return i  
    return 1 
        
input = [33, 90, 45, 12 , 15, 21, 48]
print(gcd_of_arry(input))