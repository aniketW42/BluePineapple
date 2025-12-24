# Write a python function to count all the substrings starting and ending with same characters.

import re
def CountAllSubstringsStartingAndEndingWithSameChar(string):
    scount = []
    string = re.sub(r"\s", "", string)

    while string:
        count = string.count(string[0])
        scount.append(count*(count+1)//2)
        string = re.sub(string[0],"", string)
        
    return sum(scount)
    

    

print(CountAllSubstringsStartingAndEndingWithSameChar("abbba caac pqrs mnop abca 0abc0 0abc abc0"))
    
print(CountAllSubstringsStartingAndEndingWithSameChar("aaa"))

