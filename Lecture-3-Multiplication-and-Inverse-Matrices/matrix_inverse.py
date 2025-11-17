import numpy as np

# Define a 3x3 matrix
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]], dtype=float)

print("Matrix A:")
print(A)

# Compute the inverse of A (if it exists)
A_inv = np.linalg.inv(A)

print("\nInverse of A:")
print(A_inv)

# Check A * A_inv = Identity matrix
identity_check = np.dot(A, A_inv)

print("\nA * A_inv (should be close to identity):")
print(identity_check)

# Check A_inv * A as well
identity_check_2 = np.dot(A_inv, A)

print("\nA_inv * A (should also be close to identity):")
print(identity_check_2)