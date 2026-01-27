# Write a python function to find the maximum difference between any two elements in a given array.


def find_max_difference_between_any_two_elements(lst: list) -> int | float:

    if len(lst) <= 1:
        return None

    min_ele = min(lst)
    max_ele = max(lst)

    max_diff = max_ele - min_ele

    return max_diff


if __name__ == "__main__":
    print(find_max_difference_between_any_two_elements([2, 1, 5, 3]))
    print(find_max_difference_between_any_two_elements([-10, 4, -9, -5]))
