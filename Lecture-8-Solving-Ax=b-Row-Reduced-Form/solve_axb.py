"""
Lecture 8: Solving Ax = b using Row Reduced Echelon Form
"""

import sympy as sp

# Define matrix A and vector b
A = sp.Matrix([
    [1, 2, 1],
    [2, 4, 0],
    [3, 6, 1]
])

b = sp.Matrix([
    4,
    2,
    7
])

print("Matrix A:")
print(A)
print("\nVector b:")
print(b)

# Create augmented matrix
augmented = A.row_join(b)

print("\nAugmented Matrix [A | b]:")
print(augmented)

# Compute RREF
rref_matrix, pivots = augmented.rref()

print("\nRREF of [A | b]:")
print(rref_matrix)
print("\nPivot columns:", pivots)

# Nullspace of A
nullspace = A.nullspace()

print("\nNullspace basis vectors:")
for v in nullspace:
    print(v)
