import math
def isNonPrime(nums):
    for num in nums :
        if num <=1 :
            print(num, "is non-prime")
            continue

        for i in range(2, int(math.sqrt(num)+1)):
            if num%i == 0:
                print(num, "is non-prime")
                break
        else:
            print(num, "is prime")
    
isNonPrime([1,2,3,4,5,6,7,8,9,10])