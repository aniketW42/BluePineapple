#Write a function to check whether it follows the sequence given in the patterns array.

'''
Pattern example:
For color1 = ["red", "green", "green"] and patterns = ["a", "b", "b"]
the output should be samePatterns(color1, patterns) = true;
For color2 = ["red", "green", "greenn"] and patterns = ["a", "b", "b"]
the output should be samePatterns (strings, color2) = false

'''

def is_pattern_same(strings, pattern):
    
    ps_map = {}
    p_set = set()
    
    for i in range(len(strings)):
        if strings[i] in ps_map and ps_map.get(strings[i]) != pattern[i]:
            return False
        
        elif strings[i] not in ps_map:
            if pattern[i] in p_set:
                return False
            
            ps_map[strings[i]] = pattern[i]
            p_set.add(pattern[i])

    return True

print("1", is_pattern_same(["red", "green", "green"], ["a", "b", "b"])) 

print("2", is_pattern_same(["red", "green", "greenn"], ["a","b","b"]))
            
print("3", is_pattern_same([], []))

print("4", is_pattern_same([1, 2, 2], [1, 3, 3])) 



