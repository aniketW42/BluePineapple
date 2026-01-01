# Write a function to sort each sublist of strings in a given list of lists using lambda function.

def sort_sublists(lists: list[list[str]]) -> list[list[str]]:
    
    list(map(lambda list : list.sort(), lists)) # inplace sort, map aplies the lambda function to each list in lists


if __name__ == "__main__":
    
    lists = [['a', 'z', 'q'], ['d','l','y'], ['p','o','b','w']]
    sort_sublists(lists)
    print(lists)