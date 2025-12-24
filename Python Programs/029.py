#Write a python function to find the element occurring odd number of times.

def oddFreq(li):
    freq = {}
    result = []
    for ele in li:
        freq[ele] = freq.get(ele,0) + 1
    for key, val in freq.items():
        if(val%2!=0):
            result.append(key)

    return result

print(oddFreq([1,1,1,2,2,3,3,3,3,3,4,4,5]))