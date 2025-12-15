import sympy as sp

# Define matrix A
A = sp.Matrix([
    [1, 2, 3, 1],
    [1, 1, 2, 1],
    [1, 2, 3, 1]
])

print("Matrix A:")
sp.pprint(A)

# Compute A transpose
A_T = A.T

print("\nTranspose of A (A^T):")
sp.pprint(A_T)

# Left null space = null space of A^T
left_nullspace = A_T.nullspace()

print("\nLeft Null Space vectors:")
for vec in left_nullspace:
    sp.pprint(vec)
