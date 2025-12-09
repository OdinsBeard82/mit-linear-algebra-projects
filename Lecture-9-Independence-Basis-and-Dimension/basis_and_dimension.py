"""
Lecture 9: Independence, Basis, and Dimension
"""

import sympy as sp

# Define a matrix
A = sp.Matrix([
    [1, 2, 3],
    [2, 4, 6],
    [1, 1, 1]
])

print("Matrix A:")
print(A)

# Rank
print("\nRank of A:", A.rank())

# Column space basis
col_basis = A.columnspace()
print("\nBasis for the Column Space:")
for v in col_basis:
    print(v)

# Nullspace basis
null_basis = A.nullspace()
print("\nBasis for the Nullspace:")
for v in null_basis:
    print(v)

print("\nDimension of Column Space:", len(col_basis))
print("Dimension of Nullspace:", len(null_basis))
