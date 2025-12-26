#Write a function to find the nth octagonal number.

def nth_octagonal(n):
    octagonal = 3*n**2 - 2*n
    return octagonal

print(nth_octagonal(5))

