#Write a function to find the similar elements from the given two tuple lists.

def findSimilarEle(tup1, tup2):
    similar = []
    for ele in tup1:
        if ele in tup2:
            similar.append(ele)
    return similar

print(findSimilarEle((1, 2, 3, 4), (3, 4, 5, 6)))
