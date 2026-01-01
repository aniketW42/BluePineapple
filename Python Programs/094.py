#Write a function to extract the index minimum value record from the given tuples.

"""Returning the record (tuple) that has the minimum value at a given index"""

def index_min_record(tuples, index):
    min_tuple = None
    min_val = None
    
    for tup in tuples:
        if index < len(tup):
            if not min_val or tup[index] < min_val:
                min_val = tup[index] 
                min_tuple = tup

    return min_tuple

print(index_min_record([(5,6), (1,3), (8,4), (4,2)], 1))
print(index_min_record([(5,6), (1,3), (8,4), (4,2)], 0))
print(index_min_record([(5,6), (1,3), (8,4), (4,2)], 2))
