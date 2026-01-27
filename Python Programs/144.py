# Write a python function to find the sum of absolute differences in all pairs of the given array.


def pairwiseAbsoluteDifferenceSum(li: list) -> int:

    n = len(li)
    summation = 0
    for i in range(n):
        for j in range(i, n):
            summation += abs(li[i] - li[j])

    return summation


if __name__ == "__main__":
    print(pairwiseAbsoluteDifferenceSum([9, 2, 14]))
    print(pairwiseAbsoluteDifferenceSum([1, 2, 3, 4]))
