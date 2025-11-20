# Lecture 6 – Column Space and Nullspace (MIT 18.06)

## Key Ideas

### **1. Column Space (C(A))**
The set of all linear combinations of the columns of A.  
Represents all possible outputs of the transformation Ax.

- If A is m×n, then C(A) is a subspace of ℝᵐ.
- Pivot columns form a basis for the column space.

### **2. Nullspace (N(A))**
All vectors x such that Ax = 0.

- Nullspace is a subspace of ℝⁿ.
- Contains all solutions to the homogeneous system.
- Free variables → special solutions → basis for nullspace.

### **3. Rank**
Number of pivots = dimension of the column space.

### **4. Rank–Nullity Theorem**
For an m×n matrix A:

rank(A) + nullity(A) = n


### **5. Solving Ax = 0**
- Use row reduction to identify pivot & free variables.
- Express general solution as combination of special solutions.

---

## Example from the Lecture

Given:

A =
[1 2 3]
[2 4 6]
[1 1 1]


- Rank = 2  
- One free variable → nullity = 1  
- Column 1 and column 3 are pivot columns  
- Nullspace basis includes vector like:

[-1
1
0]


(Example varies per system.)

---

## Notes
This lecture sets up the foundation for understanding the **4 Fundamental Subspaces** coming in Lecture 10.

