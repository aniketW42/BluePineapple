# Write a function to find common elements in given nested lists. * list item * list item * list item * list item

def common_elements(lists: list[list]) -> list:
    if not lists:
        return []

    sets = [set(li) for li in lists]
    commons = []

    for ele in sets[0]:
        if all(ele in li for li in sets[1:]):
            commons.append(ele)

    return commons


if __name__ == "__main__":
    print(common_elements([[1, 2, 3, 4], [2, 5, 7, 3], [9, 8, 7, 2, 3]]))
    print(common_elements([]))
