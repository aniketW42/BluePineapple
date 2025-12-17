#Write a python function to find binomial co-efficient.
def fact(n):
    if n < 0: return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def binomialCoe(n,k):
    if n<k: return None
    return fact(n) / (fact(k)*fact(n-k))

print(binomialCoe(5, 2))