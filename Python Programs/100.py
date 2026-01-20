# Write a function to find the next smallest palindrome of a specified number.

def next_smallest_palindrome(number: int) -> int:
    res = number
    while str(res) != str(res)[::-1]:
        res+=1

    return res
    
    

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