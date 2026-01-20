# Write a function to find the triplet with sum of the given array


def find_triplet_with_sum(array: list[int], target_sum: int) -> tuple[int, int, int]:
    n = len(array)
    result = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if array[i] + array[j] + array[k] == target_sum:
                    result.append([array[i], array[j], array[k]])

    return result


if __name__ == "__main__":
    print(find_triplet_with_sum([7, 5, 1, 9, 4, 8, 6, 2], 15))
    print(find_triplet_with_sum([7, 5, 1, 9, 4, 8, 6, 2], 0))
    print(find_triplet_with_sum([], 0))
