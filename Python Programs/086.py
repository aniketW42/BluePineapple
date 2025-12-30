#Write a function to find nth centered hexagonal number.

def centerd_hexagonal_number(n):
    
    hn = (3 * n**2) - 3*n + 1

    return hn

for i in range(6):
    print(centerd_hexagonal_number(i))