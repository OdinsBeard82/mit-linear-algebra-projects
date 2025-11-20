# Lecture 5: Transposes, Permutations, and Spaces ℝⁿ

This lecture covers three major ideas from MIT 18.06:

## 1. The Transpose of a Matrix
The transpose of a matrix flips rows into columns.

If  
A =  
[ a b c ]  
[ d e f ]

Then  
Aᵀ =  
[ a d ]  
[ b e ]  
[ c f ]

Key points:
- (Aᵀ)ᵀ = A  
- (AB)ᵀ = Bᵀ Aᵀ  
- Transposes appear everywhere in ML (gradients, covariance matrices, least squares).

---

## 2. Permutation Matrices
A permutation matrix is a matrix that **reorders rows** of another matrix.

Example:  
Swapping row 1 and row 3:

P =  
[ 0 0 1 ]  
[ 0 1 0 ]  
[ 1 0 0 ]

Applying it:

P * A = A but with rows reshuffled.

Permutation matrices:
- Are square  
- Have exactly one “1” in each row/column  
- Are orthogonal (Pᵀ = P⁻¹)

Used in:
- Gaussian elimination (pivoting)  
- LU factorization (tracking row swaps)

---

## 3. Spaces ℝⁿ
We also begin thinking of vectors as points in **n-dimensional space**, not just columns of numbers.

Concepts introduced:
- Columns of a matrix live in **column space**  
- Rows of a matrix live in **row space**  
- Permutations move vectors around without changing their length  
- Transposes change row/column viewpoints of the same space

This sets up the big ideas later:
- Rank  
- Nullspace  
- Fundamental subspaces  

---

## Summary
Lecture 5 introduces the geometric and algebraic roles of:
- Transpose  
- Permutation matrices  
- Vector spaces ℝⁿ  

These ideas form the backbone for everything coming in Lectures 6–10.
