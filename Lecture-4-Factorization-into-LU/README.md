# Lecture 4: Factorization into A = LU

This folder contains the Python implementation and notes for **Lecture 4 of MIT 18.06 Linear Algebra**.

## Summary
This lecture introduces **LU factorization**, where a matrix A is written as:

A = L · U  
L → lower-triangular  
U → upper-triangular  

This factorization makes solving linear systems easier and forms a core tool in numerical linear algebra.

---

## Python Implementation
- `lu_factorization.py` — Computes the LU factorization of a matrix using Python (`scipy.linalg.lu`) and verifies that L · U reconstructs A.

Example matrices are taken from the lecture.

---

## Example Output
L matrix:
[[ 1. 0. 0. ]
[ 0.67 1. 0. ]
[ 0.33 0.5 1. ]]

U matrix:
[[ 6. 18. 22.]
[ 0. -5. -7. ]
[ 0. 0. -3. ]]


(L × U ≈ A)

---

## Notes
See `lecture4_notes.md` for a breakdown of:
- LU factorization  
- Why it works  
- How it relates to elimination  
- Why it matters for AI / Machine Learning  

---

## AI / ML Relevance
LU factorization is widely used in:
- Linear regression  
- Matrix solvers  
- Optimization algorithms  
- Core numerical routines in ML libraries  

Understanding LU builds the mathematical foundation for deeper ML topics later on.

