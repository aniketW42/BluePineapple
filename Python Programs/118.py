# write a function to convert a string to a list.


def str_to_list(string: str) -> list:
    list_str = [ch for ch in string]
    return list_str

if __name__ == '__main__':
    print(str_to_list("Python"))
    print(str_to_list(""))