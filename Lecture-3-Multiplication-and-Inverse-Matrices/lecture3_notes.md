# Lecture 3: Multiplication and Inverse Matrices

## Key Concepts

### Matrix Multiplication
- Rows of the first matrix interact with columns of the second matrix.
- Each entry represents a weighted combination of columns.
- Multiplication is **not commutative** (AB ≠ BA).
- Geometric view: matrices transform vectors into new vectors.

### Identity Matrix
- Acts like “1” for matrices.
- AI = IA = A.

### Inverse Matrix
- A matrix A has an inverse A⁻¹ only if its determinant ≠ 0.
- A⁻¹ satisfies: A · A⁻¹ = I and A⁻¹ · A = I.
- The inverse gives a direct solution to Ax = b → x = A⁻¹b.

### Practical Notes
- Not all matrices are invertible (singular matrices have no inverse).
- In numerical computing, we rarely compute A⁻¹ directly — but for learning, it’s useful.

## Python Implementation
- Computed matrix inverse using `numpy.linalg.inv`.
- Multiplied A · A⁻¹ and confirmed it equals the identity matrix.
- Demonstrates how linear transformations behave when reversed.
