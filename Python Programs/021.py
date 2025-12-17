#Write a function to find m number of multiples of n.

def mMultiplesOfn(m, n):
    result = []
    for i in range(1, m+1):
        result.append(n*i)
    return result

print(mMultiplesOfn(20,2))
