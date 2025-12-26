#Write a function to find the number of ways to partition a set of bell numbers.

def positive_sum(li):
    return sum([ele for ele in li if abs(ele)==ele])

print(positive_sum([1,1,1,1,-1,-1,-1,-1,-2,-2,-63,-12,10]))