# Write a function to sort a list of elements using pancake sort.


def flip(arr, k):
    return arr[0 : k + 1][::-1] + arr[k + 1 :]


def max_index(arr):
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx


def pancake_sort(array):
    n = len(array)

    for i in range(n):
        max_idx = max_index(array[: n - i])
        array = flip(array, max_idx)
        array = flip(array, n - i - 1)

    return array


if __name__ == "__main__":
    print(pancake_sort([3, 2, 4, 1]))
    print(pancake_sort([]))
    print(pancake_sort([1,1]))
    print(pancake_sort([1]))
    print(pancake_sort([4, 1, 7, 3, 5, 2, 6]))
