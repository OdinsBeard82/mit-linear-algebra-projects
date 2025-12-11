import numpy as np

# Coefficient matrix (the numbers in front of x, y, z)
A = np.array([[2, 1, 0],
              [-3, -1, 2],
              [-2, 1, 2]])

# Right-hand side constants
b = np.array([8, -11, -3])

# Solve Ax = b
x = np.linalg.solve(A, b)

# Print the solution
print("Solution:")
print(f"x = {x[0]}, y = {x[1]}, z = {x[2]}")
