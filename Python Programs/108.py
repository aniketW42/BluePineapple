# Write a function to merge multiple sorted inputs into a single sorted iterator using heap queue algorithm.

import heapq


def merge_sorted_inputs(inputs: list[tuple | list | dict | set]) -> list:
    merged = heapq.merge(*inputs)
    return list(merged)


if __name__ == "__main__":
    print(merge_sorted_inputs([[1, 2, 3, 4], (4, 6, 7, 8), [5, 9, 10, 11]]))
    print(merge_sorted_inputs([[5, 9, 10, 11], [1, 2, 3, 4], (4, 6, 7, 8)]))
    print(merge_sorted_inputs([[5, 9, 10, 11], [1, 2, 3, 4], {4, 6, 7, 8}]))
    print(
        merge_sorted_inputs(
            [[5, 9, 10, 11], [1, 2, 3, 4], {4, 6, 8}, {1: "1", 2: "2", 3: "3"}]
        )
    )
