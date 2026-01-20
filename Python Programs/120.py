# Write a function to find the maximum product from the pairs of tuples within a given list.


def find_max_product_of_pairs(pairs: list[tuple[int | float, int | float]]) -> int | float:

    if not pairs:
        return None
    
    max_product = pairs[0][0] * pairs[0][1]

    for pair in pairs:
        product = pair[0] * pair[1]

        if product > max_product:
            max_product = product

    return max_product


if __name__ == "__main__":

    print(find_max_product_of_pairs([(7, 5), (4, 9), (4, 6), (8, 2), (6, 4)]))
    print(find_max_product_of_pairs([(7, -5), (4, -9), (-4, 6), (8, -2), (-6, 4)]))
    print(find_max_product_of_pairs([(),()]))
