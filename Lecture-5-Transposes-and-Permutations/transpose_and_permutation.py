import numpy as np

# Example matrix A
A = np.array([
    [1, 4, 2],
    [3, 5, 7],
    [6, 9, 8]
], dtype=float)

print("Original Matrix A:")
print(A)

# Transpose of A
A_T = A.T
print("\nTranspose of A (A^T):")
print(A_T)

# Example permutation matrix (swap row 1 and row 3)
P = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
], dtype=float)

print("\nPermutation Matrix P (swaps rows):")
print(P)

# Apply permutation: P * A
PA = P @ A
print("\nPermutation Applied (P * A):")
print(PA)

# Check orthogonality: P^T = P^-1
print("\nP^T (transpose of permutation matrix):")
print(P.T)

print("\nP^T * P (should be identity):")
print(P.T @ P)
