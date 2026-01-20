# Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.

# to check if num = 2^x + 2^y +2^x ... {x, y, z,..} != 0

# any even number (num>0) can be represented and 2^1 + 2^1 + ......

def check_if_number_can_be_represented_as_sum_of_nonzero_powers_of_two(number: int) -> bool:
    
    return number > 0 and number%2 == 0

if __name__ == "__main__":
    print(check_if_number_can_be_represented_as_sum_of_nonzero_powers_of_two(30))
    print(check_if_number_can_be_represented_as_sum_of_nonzero_powers_of_two(16))
    print(check_if_number_can_be_represented_as_sum_of_nonzero_powers_of_two(50))
    print(check_if_number_can_be_represented_as_sum_of_nonzero_powers_of_two(17))
    print(check_if_number_can_be_represented_as_sum_of_nonzero_powers_of_two(23))





        


