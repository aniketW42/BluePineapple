# Write a function to multiply all the numbers in a list and divide with the length of the list.

def multiply_all_and_divide_by_len(numbers: list[int]) -> float:
    
    if not numbers:
        return 'undefined'

    mult = 1
    for number in numbers:
        mult *= number

    return mult/len(numbers)
    


if __name__ == "__main__":
    print(multiply_all_and_divide_by_len([1, 2, 3, 4 ,5 ,6]))

