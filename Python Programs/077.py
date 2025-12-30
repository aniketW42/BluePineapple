#Write a python function to find the difference between sum of even and odd digits.

def evenOdd_sum_diff(digits):
    evensum = 0
    oddsum = 0

    for digit in digits:
        if digit%2 ==0:
            evensum += digit
        else:
            oddsum += digit

    return evensum - oddsum


print(evenOdd_sum_diff([2,3,7,5,6,4,9]))
print(evenOdd_sum_diff([2,3,7,5,6,4,9]))
