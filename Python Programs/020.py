#Write a function to check if the given number is woodall or not.
def isWoodall(num):
    if(type(num)!=int or num%2==0 or num<1): return False
    temp = num + 1
    count = 0
    while temp != count:
        if(temp<=0):
            return False
        temp/=2
        count+=1
    
    return True
    
print(isWoodall(383))
print(isWoodall(31))
