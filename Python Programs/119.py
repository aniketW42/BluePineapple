# Write a python function to find the element that appears only once in a sorted array.

def elements_that_appeared_once(array: list) -> list:
    arr_length = len(array)
    once = []
    for i in range(arr_length):
        curr = array[i]
        prev = None
        next = None

        if i > 0:
            prev = array[i - 1]
        if i < arr_length - 1:
            next = array[i + 1]

        if curr != prev and curr != next:
            once.append(curr)

    return once


print(elements_that_appeared_once([1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9]))
print(elements_that_appeared_once(["a", "b", "c", "c", "d", "e", "e", "e", "f"]))
