#Write a function to find the maximum difference between available pairs in the given tuple list.

def max_diff(pairs):
    if pairs:
        md = abs(pairs[0][0] - pairs[0][1])
        for pair in pairs:
            diff = abs(pair[0] - pair[1])
            if md < diff:
                md = diff
        return md
    else: return None

print(max_diff([(5,6),(7,6),(8,80),(221,288)]))
print(max_diff([]))