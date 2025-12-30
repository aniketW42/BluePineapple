#Write a python function to count the number of squares in a rectangle.

# def count_squares_in_rectangle(h, w):
    
#     count = 0

#     for i in range(1, min(h,w)+1):
#         count += i**2

#     extra = abs(h-w)
#     if extra == 0:
#         return count
    
#     else:
#         count = count + count_squares_in_rectangle(min(h,w), extra)

#     return count
    

def count_squares_in_rectangle(h, w):
    
    count = 0

    for i in range(0, min(h,w)):
        count += (h-i) * (w-i)

    return count


print("6x4 : ",count_squares_in_rectangle( 6,4))
print("2x2 : ",count_squares_in_rectangle( 2,2))
print("4x3 : ",count_squares_in_rectangle( 4,3))
print("0x0 : ",count_squares_in_rectangle( 0,0))
