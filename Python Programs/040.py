#Write a function to find frequency of the elements in a given list of lists using collections module.
from collections import Counter
def freq(li):
    return Counter(li)

print(freq([1,2,3,1,2,4,5,4,5,8]))