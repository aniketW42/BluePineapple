#Write a function to sort a list of tuples using lambda.

def sort_using_lambda(tuli):
    return sorted(tuli, key = lambda x: x[0] if x else float('inf'))

tuli = [(5,4,3), (42,56,12),(75,36,86,52)]
print(sort_using_lambda(tuli))
print(sort_using_lambda([(46,16,76,42,37,16,34), (463,491,971,338,641,316),(16,43,16,56,153,63,23)]))
print(sort_using_lambda([]))
print(sort_using_lambda([(), (),()]))
