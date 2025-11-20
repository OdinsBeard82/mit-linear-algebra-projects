"""
Lecture 6: Column Space and Nullspace
Compute the column space, row-reduced form, and nullspace of a matrix.
"""

import numpy as np
from sympy import Matrix

# Define a sample matrix A
A = Matrix([
    [1, 2, 3],
    [2, 4, 6],
    [1, 1, 1]
])

print("Matrix A:")
print(np.array(A), "\n")

# Column space
col_space = A.columnspace()
print("Column Space basis vectors:")
for v in col_space:
    print(np.array(v), "\n")

# Nullspace
null_space = A.nullspace()
print("Nullspace basis vectors:")
for v in null_space:
    print(np.array(v), "\n")

# Rank
print(f"Rank of A: {A.rank()}")
print(f"Nullity of A: {A.nullspace()[0].shape[0] if null_space else 0}")
