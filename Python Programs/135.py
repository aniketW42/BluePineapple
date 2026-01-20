# Write a function to find the nth hexagonal number.

# 1, 6, 15, 28, 45, etc

# n *(2*n -1 )


def nth_hexagonal_number(n):

    nth_hex_num = n * (2 * n - 1)
    return nth_hex_num


for i in range(1,11):
    print(nth_hexagonal_number(i))