# Write a function to find number of lists present in the given tuple.

def count_lists_in_tuple(tup: tuple) -> int:
    count = 0
    for iterable in tup:
        if isinstance(iterable, list):
            count+=1

    return count

if __name__ == "__main__":
    print(count_lists_in_tuple(([1,2], 5, {"a", 1}, {8, 2}, [2, 1], [])))
    print(count_lists_in_tuple((5, {"a", 1}, {8, 2})))
    print(count_lists_in_tuple(("name", "string", ["string"])))