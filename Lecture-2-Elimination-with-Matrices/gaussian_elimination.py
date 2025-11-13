"""
Lecture 2: Elimination with Matrices
Python implementation of Gaussian elimination for solving a linear system.
"""

import numpy as np

def gaussian_elimination(A, b):
    """
    Solves Ax = b using Gaussian elimination
    """
    n = len(b)
    M = np.hstack([A.astype(float), b.reshape(-1, 1)])

    # Forward elimination
    for i in range(n):
        # Normalize pivot row
        M[i] = M[i] / M[i, i]
        # Eliminate entries below pivot
        for j in range(i + 1, n):
            M[j] = M[j] - M[j, i] * M[i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = M[i, -1] - np.dot(M[i, i+1:n], x[i+1:n])

    return x

# Example system
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])

solution = gaussian_elimination(A, b)

# Print system and solution
print("System:")
print("2x + y - z = 8")
print("-3x - y + 2z = -11")
print("-2x + y + 2z = -3\n")
print("Solution:")
print(f"x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")
