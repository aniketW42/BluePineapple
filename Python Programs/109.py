# Write a python function to find the count of rotations of a binary string with odd value.

def count_odd_binary_rotations2(binary_str: str) -> int:  # more optimized solution
    count = binary_str.count("1")
    return count


def count_odd_binary_rotations1(binary_str: str) -> int:
    n = len(binary_str)
    count = 0

    for i in range(n):
        binary_str = binary_str[-1] + binary_str[:-1]
        if binary_str[-1] == "1":
            count += 1

    return count


if __name__ == "__main__":
    print(count_odd_binary_rotations1("1011"))
    print(count_odd_binary_rotations2("1011"))
