# Write a python function to find whether the given number is present in the infinite sequence or not.

"""
Given three integers A, D and N. In an infinite sequence, A is the first number, D is the common difference. The task is to check if the number N will appear in the sequence or not.

nth term in sequence is : Tn = A + (n-1) D

 n - 1 = (Tn - A) / D
 n = [ (Tn-A)/D ] + 1 

 if n is integer then the number N is present in the sequence

"""

def is_present(A: float, D: float, N: float)-> bool:
    
    n = ((N-A)//D) + 1

    Tn = A + (n - 1) * D

    print(Tn)
    
    return Tn == N

print(is_present(1, 1, 10))
    