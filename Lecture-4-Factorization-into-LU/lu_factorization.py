import numpy as np
from scipy.linalg import lu

# Matrix from the lecture
A = np.array([[2, 3, 1],
              [4, 7, 7],
              [6, 18, 22]], dtype=float)

# Perform LU decomposition
P, L, U = lu(A)

print("P matrix (Permutation):")
print(P)

print("\nL matrix (Lower-triangular):")
print(L)

print("\nU matrix (Upper-triangular):")
print(U)

print("\nReconstruct A (P @ L @ U):")
print(P @ L @ U)

print("\nOriginal A:")
print(A)
