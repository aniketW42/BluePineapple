#Write a python function to find the last digit when factorial of a divides factorial of b.


def fact(num):
    ft = 1;
    for i in range(2, num+1):
        ft *= i
    return ft

def last_digit_of_div_of_factorials(a, b):
    if a > b:
        return 0
    facta = fact(a)
    factb = fact(b)
    div = factb//facta
    return div%10
    


print(last_digit_of_div_of_factorials(0, 1)) 
print(last_digit_of_div_of_factorials(3, 4))
print(last_digit_of_div_of_factorials(5, 4))
print(last_digit_of_div_of_factorials(4, 5))
print(last_digit_of_div_of_factorials(0, 0))


