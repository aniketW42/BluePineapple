# Write a python function to check whether the last element of given array is even or odd after performing an operation p times.


def is_last_element_odd(li, p):
    
    for _ in range(p):
        li_sum = sum(li) + 1
        li.append(li_sum)

    return li[-1] % 2 == 0


print(is_last_element_odd([2, 3], 3))
