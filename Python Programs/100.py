# Write a function to find the next smallest palindrome of a specified number.

def next_smallest_palindrome(number: int) -> int:

    num_len = len(str(number))

    for i in range(num_len//2):
        str_num = str(number)
        left = int(str_num[i]) 
        right = int(str_num[len(str_num) - i - 1]) 

        if left!=right and number%10==0:
            number = number - 10**i 
        elif left < right:
            number -= (right-left) * 10**i
        elif left > right:
            number -= 10**(len(str_num)-i-1)
        # print(number)

    return number
    
        

if __name__ == "__main__":
    print("-->", next_smallest_palindrome(199))
    print("-->", next_smallest_palindrome(100))
    print("-->", next_smallest_palindrome(10000))
    print("-->", next_smallest_palindrome(1))
    print("-->", next_smallest_palindrome(10))
    print("-->", next_smallest_palindrome(1001))
    print("-->", next_smallest_palindrome(1101))
    print("-->", next_smallest_palindrome(1981))
    print("-->", next_smallest_palindrome(1011))
    print("-->", next_smallest_palindrome(94187978322))