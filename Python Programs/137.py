# Write a function to find the ratio of zeroes in an array of integers.


def find_ratio_of_zeros(array: list[int]) -> float:

    number_of_zeros = array.count(0)

    total_elements = len(array)

    ratio = number_of_zeros / total_elements

    return ratio


if __name__ == "__main__":
    print(find_ratio_of_zeros([1, 2, 3, 0, 4, 0, 6, 9, 0, 4]))
