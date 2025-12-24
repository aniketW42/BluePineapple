#Write a python function to check whether the first and last characters of a given string are equal or not.


def is_startNend_equal(string):
    
    return bool(string) and string[0] == string[-1]
    
print(is_startNend_equal("")) 
print(is_startNend_equal("this is string")) 
print(is_startNend_equal("that is it")) 
print(is_startNend_equal("That is it")) 