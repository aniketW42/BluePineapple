#Write a function to find the nth tetrahedral number

def nth_treahedral_num(n):

    tn = n*(n+1)*(n+2) // 6

    return  tn


for i in range(11):
    print(nth_treahedral_num(i))

