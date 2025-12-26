#Write a python function to find the largest number that can be formed with the given digits.

def largest_num_using_given_digits(digs):
    largest_num = 0

    while digs:
        m = max(digs)
        largest_num = largest_num*10 + max(digs)
        digs.remove(m)

    return largest_num

print(largest_num_using_given_digits([6,7,1,2,4,6,9]))


