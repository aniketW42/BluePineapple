# Write a function to find frequency count of list of lists.

# solution 1
def frequency_count1(lists : list[list]) -> list[tuple[list, int]] :
    freq = []
    visited = []

    for li in lists:
        if li not in visited:
            freq.append((li, lists.count(li)))
            visited.append(li)

    return freq

# solution 2 (more efficient)
from collections import Counter
def frequency_count2(lists: list[list])  -> list[tuple[list, int]] :
    counts = Counter(tuple(li) for li in lists)
    
    return [ (list(k), v) for k, v in counts.items() ]


print(frequency_count1([[1,2], [2,3], [1,2], [4,6], []]))
print(frequency_count2([[1,2], [2,3], [1,2], [4,6], []]))