#Write a python function to find the nth digit in the proper fraction of two given numbers.
def nth_digit(numerator, denominator, n):

    ans = numerator%denominator
    # print(ans)
    for _ in range(n):
        ans = ans*10
        dig = ans//denominator
        ans = ans%denominator

    return dig

print(nth_digit(1,3,50))