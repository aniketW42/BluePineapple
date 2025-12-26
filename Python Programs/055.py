#Write a function to find t-nth term of geometric series.

def geometric_nth_term(a, r, n):
    return a * (r ** (n - 1))

print(geometric_nth_term(2,3,20))