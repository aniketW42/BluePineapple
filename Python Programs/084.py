#Write a function to find the n-th number in newman conway sequence

def p_n(n):

    if n==1 or n==2:
        return 1
    
    pn_mo = p_n(n-1)
    pn_mpn_mo = p_n(n - pn_mo)

    pn = pn_mo(pn_mo+pn_mpn_mo)

    return pn


for i in range(1, 21):
    print(p_n(i))
