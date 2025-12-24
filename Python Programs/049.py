#Write a function to extract every first or specified element from a given two-dimensional list.
def extract_ele(mat, row=None, col=None):
    if mat:
        if row and col:
            try:
                return mat[row][col]
            except IndexError as e:
                print(e)
        else:
            return [row[0] for row in mat]

# extract specified ele
print(
    extract_ele([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ], 2, 2)
)

#extract every first ele
print(
    extract_ele([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])
)

