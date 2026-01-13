# Write a function to extract the ranges that are missing from the given list with the given start range and end range values.

def extract_missing_range(numbers: list[int]) -> list[tuple]:
    ranges = []

    # Assumming the list is sorted
    for i in range(1, len(numbers)):
        if numbers[i] - 1 != numbers[i - 1]:
            ranges.append((numbers[i - 1] + 1, numbers[i]-1)) # [start, end] -> both inclusive
    
    return ranges


if __name__ == "__main__":
    print(extract_missing_range([-1, 1, 2, 3, 6, 7, 8, 11, 12, 19]))
