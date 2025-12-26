#Write a function of recursion list sum.

def recursion_sum(li):
    if not li:
        return 0
    sum = li[0] + recursion_sum(li[1:])
    return sum

print(recursion_sum([1,2,3,4,5,6]))
print(recursion_sum([]))