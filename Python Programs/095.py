# Write a python function to find the minimum length of sublist.

def min_length_of_sublist(lists):

    min_len = len(min(lists, key=len))

    return min_len

print(min_length_of_sublist([[1,3,4,6], [1,2,3], [3,4,6,2,1]]))
print(min_length_of_sublist([[1,3,4,6], [1,2,3,6], [3,6]]))
print(min_length_of_sublist([[], [1,2,3], [3,4,6], [1]]))