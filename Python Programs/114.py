# Write a function to assign frequency to each tuple in the given tuple list.
from collections import Counter
def tuple_frequency_count(tuples: list[tuple]) -> dict[tuple, int]:
    freq = Counter(tuples)
    return freq


if __name__ == '__main__':
    print(tuple_frequency_count(
        [(1, 2, 3), (4, 5), (7, 8, 9), (1, 2, 3), (1, 2, 3), (), (2,), (4, 5)])
    )