#Write a function to check if the given tuple list has all k elements.

def hasallk(tuplist, ks):
    ts = set().union(*tuplist)
    for ele in ks:
        if ele not in ts:
            return False
    return True

print(hasallk([(0,1,2),(3,4),(5,6)], [1,2,3]))