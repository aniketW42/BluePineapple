# Write a function to check whether all dictionaries in a list are empty or not.

def are_all_dicts_empty(dicts: list[dict]) -> bool:
    return all(len(dict)==0 for dict in dicts)

if __name__ == '__main__':
    print(are_all_dicts_empty([{}, {}, {}, {}]))
    print(are_all_dicts_empty([{}, {}, {}, {}]))
    print(are_all_dicts_empty([{}, {}, {}, {}]))
    