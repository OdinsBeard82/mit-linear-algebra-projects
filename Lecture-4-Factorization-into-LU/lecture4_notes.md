# Lecture 4 — Factorization into A = LU

**Main idea:**  
Any matrix A can often be split (factored) into two simpler matrices:

A = L · U  
L = Lower-triangular  
U = Upper-triangular  

This factorization makes solving Ax = b much faster and easier.

---

## Why LU Factorization Matters
- Makes solving linear systems efficient  
- Allows reuse of L and U to solve multiple Ax = b problems  
- Helps understand how elimination works under the hood  
- Important for numerical methods, data science, and machine learning models

---

## Breakdown of the Concept

### 1. Start with matrix A  
Example:
A =  
[ 2   3   1 ]  
[ 4   7   7 ]  
[ 6  18  22 ]

### 2. Perform Gaussian elimination  
Instead of overwriting A like usual, we **track the multipliers**, which become the entries of L.

### 3. L Matrix  
L contains:
- 1’s on the diagonal  
- Elimination multipliers below the diagonal  

### 4. U Matrix  
U contains the final result of elimination — the upper triangular matrix.

### 5. Check the Factorization  
L × U ≈ A  
Small floating-point rounding errors are normal.

---

## Why This Matters for AI / Machine Learning
- Gradient descent relies on matrix operations  
- LU is used in optimization algorithms  
- Solving Ax = b efficiently is key in linear regression  
- Factorizations are the foundation of numerical linear algebra

---

## What You Should Know from This Lecture
- How Gaussian elimination leads directly to LU  
- The structure of L and U  
- Why LU is computationally cheaper  
- Relation to solving systems and understanding matrices at a deeper level
