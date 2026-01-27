# Write a function to extract every specified element from a given two dimensional list.

def extract_elements_from_2d_list(two_d_list, positions):

    eles = []
    for position in positions:
        
        i = position[0]
        j = position[1]
        if i < len(two_d_list) and j < len(two_d_list[i]):
            eles.append(two_d_list[i][j])
        else:
            raise IndexError()
        
    return eles

print(extract_elements_from_2d_list([[1, 2, 3], [4, 5, 6]], [(0,1), (1,2)]))