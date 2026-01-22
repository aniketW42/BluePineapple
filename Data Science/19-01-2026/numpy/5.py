"""
5. Matrix Ops (Dot, Transpose, Identity)
    Generate two matrices A (3x4) and B (4x2).
    Compute A @ B.
    Verify properties: (A.T).T equals A; create identity matrix I and show A
    @ I (shape permitting).

"""
import numpy as np

A = np.array(np.random.randint(1, 100, 12)).reshape(3, 4)
print("A:\n", A)

B = np.array(np.random.randint(1, 100, 8)).reshape(4,2)
print("\nB:\n", B)

dot_product = A @ B
print("\nDot product fo A and B:\n", dot_product)

print("\n(A.T).T equals A:", np.array_equal((A.T).T , A)  )

I = np.eye(4, dtype=int)

print("\nA @ I ->\n", A @ I )