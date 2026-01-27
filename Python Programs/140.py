# Write a function to extract elements that occur singly in the given tuple list.
from collections import Counter


def extract_non_duplicate_elements(tuple_list: list[tuple]) -> list:

    occurences = Counter()

    for tup in tuple_list:
        freq = Counter(tup)
        occurences = occurences + freq

    non_duplicate = []

    for key, val in occurences.items():
        if val == 1:
            non_duplicate.append(key)

    return non_duplicate


if __name__ == "__main__":
    print(extract_non_duplicate_elements([(1, 2, 3, 4), (1, 3, 4, 5), (2, 4, 1, 3, 9)]))
