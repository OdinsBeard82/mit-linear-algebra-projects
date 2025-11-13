"""
Lecture 1: The Geometry of Linear Equations
Python implementation of solving a linear system using NumPy.
"""

import numpy as np

# Define the coefficient matrix A and right-hand side vector b
A = np.array([[2, 1, 0],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])

# Solve Ax = b
x = np.linalg.solve(A, b)

# Print the solution
print("System:")
print("2x + y       = 8")
print("-3x - y + 2z = -11")
print("-2x + y + 2z = -3\n")
print("Solution:")
print(f"x = {x[0]}, y = {x[1]}, z = {x[2]}")
