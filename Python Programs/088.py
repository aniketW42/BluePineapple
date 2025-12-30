#Write a function to get the frequency of the elements in a list.

def freq(li):
    freq = {}
    for ele in li:
        freq[ele] = freq.get(ele, 0) + 1
    
    return freq

print(freq([1,2,1,2,1,2,3,4,5,6,6]))