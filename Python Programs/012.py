#Write a function to sort a given matrix in ascending order according to the sum of its rows.

# def sorMatrix(mat):
#     return sorted(mat, key=sum)

# print(sorMatrix([[3,4,5],[1,2,3],[0,1,2]]))



def sortMatrix(mat):
    matsum = {}
    for li in mat:
        matsum[tuple(li)] = sum(li)

    sortedmatsum = dict(sorted(matsum.items(), key = lambda x: x[1])) 
    result = []
    for key in sortedmatsum.keys():
        result.append(list(key))
    print(result)

sortMatrix([[3,4,5],[1,2,3],[0,1,2]])

    

