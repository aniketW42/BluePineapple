#Write a function to find the list with minimum length using lambda function.

def list_with_min_len(lists):

    return min(lists, key = lambda x: len(x))

print(list_with_min_len([
    [1,2,3,4,5],
    [2,4,6,7,8,5,6],
    [1,2,3,4],
    [2,3,9,7,6]
]))