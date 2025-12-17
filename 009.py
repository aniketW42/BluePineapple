#Write a python function to find the minimum number of rotations required to get the same string.

def minRotation(str):
    if len(str) < 2 : return 0
    str2 = str
    for i in range(0, len(str)):
        n = len(str2)-1
        str2 = str2[n] + str2[0:n]
        if(str2 == str) : return i+1
    return len(str)
    
test_cases = {
    "aaaa": 1,          
    "abab": 2,          
    "abcabc": 3,        
    "abcd": 4,          
    "": 0,             
    "a": 0,            
    "aa": 1,           
    "ab": 2,           
    "aba": 3,          
    "aab": 3,
    "abcab": 5,
    "AaAa": 2, 
    "aAaA": 2,
    "1111": 1,
    "1212": 2,
    "@@@@": 1,
    "@#@#": 2,
    "xyzxyzxyz": 3,
    "radar": 5,
}

for key in test_cases:
    result = minRotation(key)
    if(result==test_cases[key]):
        print("Correct")
    else:
        print(key + " : Wrong")
