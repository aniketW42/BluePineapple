# Write a function to calculate magic square.

def magicSquare(n):
    m = n*(n*n + 1)//2
    return m

print(magicSquare(3))