#Write a python function to determine whether all the numbers are different from each other are not.

def are_all_same(li):
    if len(set(li)) == 1:
        return True
    else:
        return False
    
print(are_all_same([2,2,2,2,2]))
print(are_all_same([0, -1, -1, -1]))
print(are_all_same(["1", "1", "1"]))
print(are_all_same(["1", "1", "2"]))
print(are_all_same(["a", "a", "a"]))
print(are_all_same(["a", "A", "a"]))