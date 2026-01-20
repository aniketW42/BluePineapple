# Write a function to shortlist words that are longer than n from a given list of words.


def shortlist_words_that_are_longer_than_n(words, n):

    shortlisted_words = [word for word in words if len(word) > n]

    return shortlisted_words

print(shortlist_words_that_are_longer_than_n(["hello", "this", "is", "sample", "list", "of", "strings"], 4))