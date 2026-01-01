# Write a function to add the given list to the given tuples.

def add_to_tuples(tuples: list[tuple], list_to_add) -> list[tuple]:

    return list((*tup, *list_to_add) for tup in tuples)

if __name__ == '__main__':
    print(add_to_tuples([(4,5), (9,7), (8,5)], [1,2]))

