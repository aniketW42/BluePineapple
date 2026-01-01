#Write a function to check whether the given number is undulating or not.

''' 
    If <a> represents the digit in the ones place and <b> represents the digit in the tens place, 
    an undulating number must follow an alternating pattern (...aba), thats what is implemented in this function.
'''

def is_undulating(num):
    if num%100 == 0:
        return False

    a = num%10
    b = num%100 // 10
    
    expected_num = 0
    power = 0
    while num >= expected_num:    
        expected_num =  expected_num + (a * 10**power)
        if(num==expected_num) : 
            return True
        
        power+=1
        
        expected_num = expected_num + (b * 10**power)
        if(num==expected_num) : 
            return True

        power+=1

    return False

print("121 --> ", is_undulating(121))
print("8989 --> ", is_undulating(8989))
print("9898 --> ", is_undulating(9898))
print("18989 --> ", is_undulating(18989))
print("1212 --> ", is_undulating(1212))
print("1010 --> ", is_undulating(1010))
print("0 --> ", is_undulating(0))


    
