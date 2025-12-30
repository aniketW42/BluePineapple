#Write a function to find tuples which have all elements divisible by k from the given list of tuples.

def find_tuples_divisible_by_k(tuples, k):
    if k==0:
        return None
    
    result = []
    for tuple in tuples:
        flag = True
        for ele in tuple:
            if ele%k != 0 :
                flag = False
                break

        if tuple and flag :
            result.append(tuple)
    
    return result

print(find_tuples_divisible_by_k([(2,4,6,8), (3,2,4,5,8), (16,42,31,5), (), (2,)], 2))