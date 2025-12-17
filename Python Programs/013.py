#Write a function to count the most common words in a dictionary.

def mostCommon(dictionary):
    occurrence = {}
    for word in dictionary:
        occurrence[word] = occurrence.get(word,0) + 1

    sortvals = sorted(occurrence.values())
    maxfreq = sortvals[-1]
    result = []
    for key, value in occurrence.items():
        if value == maxfreq : result.append(key)

    return result

print(mostCommon(["hello", "this", "hello", "one", "one"]))

