"""
Lecture 7: Solving Ax = 0 — Pivot Variables & Special Solutions
"""

import sympy as sp

# Example matrix from Lecture 7-style structure
A = sp.Matrix([
    [1, 2, 3, 1],
    [2, 4, 6, 2],
    [1, 1, 1, 0]
])

print("Matrix A:")
print(A)
print("\nRow-Reduced Form (RREF):")
rref_matrix, pivots = A.rref()
print(rref_matrix)
print("\nPivot columns:", pivots)

# Nullspace basis (special solutions)
null_basis = A.nullspace()
print("\nNullspace basis vectors:")
for v in null_basis:
    print(v)

print(f"\nRank: {A.rank()}")
print(f"Nullity: {len(null_basis)}")
