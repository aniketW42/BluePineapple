# Write a function to find the longest subsequence such that the difference between adjacents is one for the given array.

def longest_subsequence_with_adjacent_difference_one(array: list[int]) -> list[int]:

    start = 0
    end = 0
    n = len(array)
    subsequence = []

    for i in range(1, n):
        if abs(array[i] - array[i-1]) == 1:
            end+=1
            if i+1 == n:
                subsequence.append((start, end))
        else:
            if end > start:
                subsequence.append((start, end))
            start = i
            end = i

    longest_subsequence_indices = max(subsequence, key = lambda x: x[1] - x[0]) 

    return array[longest_subsequence_indices[0]:longest_subsequence_indices[1]+1]

if __name__ == "__main__":
    print(longest_subsequence_with_adjacent_difference_one([1,2,3,4,5,9]))
    print(longest_subsequence_with_adjacent_difference_one([1,2,3,4,5,6]))
    print(longest_subsequence_with_adjacent_difference_one([1,3,2,3,5,6,7,8]))
    print(longest_subsequence_with_adjacent_difference_one([1,3,2,3,5,6,7,8]))