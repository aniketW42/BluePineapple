# Write a function to find the item with maximum frequency in a given list.


def item_with_max_frequency1(li):
    if not li:
        return

    freq = {}
    target = [] # [item, count]
    for item in li:
        freq[item] = freq.get(item, 0) + 1

        if not target:
            target = [item, freq[item]]
        elif freq[item] > target[1]:
            target[1] = freq[item]
            target[0] = item

    return target[0]


def item_with_max_frequency2(li):
    if not li:
        return

    target_item = li[0]
    target_item_count = li.count(target_item)
    for item in li:
        item_count = li.count(item)
        if item_count > target_item_count:
            target_item_count = item_count
            target_item = item

    return target_item


print(item_with_max_frequency1([1, 2, 1, 2, 1, 3, 4, 5, 6, 3, 3, 3, 3]))
print(item_with_max_frequency2([1, 2, 1, 2, 1, 1, 3, 4, 5, 6, "3", "3","3","3"]))
