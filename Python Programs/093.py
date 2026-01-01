#Write a function to calculate the value of 'a' to the power 'b'.

def power(a, b):
    if(a==0 and b<0):
        raise ValueError("0 cannot be raised to power zero")
        
    return a**b


print(power(2,2))
print(power(2,3))
print(power(5,2))
print(power(5,0))
print(power(0,2))
# print(power(0,-2))
print(power(1,-2))
print(power(2,-2))