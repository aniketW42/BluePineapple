# Write a function to convert tuple to a string.

def tuple_to_string(tup):
    return "".join(str(ele) for ele in tup)

print(tuple_to_string(("1","2","3")))
print(tuple_to_string((1,2,3)))