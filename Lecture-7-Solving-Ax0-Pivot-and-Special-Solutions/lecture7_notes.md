# Lecture 7 – Solving Ax = 0: Pivot Variables & Special Solutions (MIT 18.06)

## Key Ideas

### **1. Homogeneous System: Ax = 0**
We’re solving for all x that satisfy the equation.

- Always has at least one solution: the zero vector.
- The interesting part is when there are non-trivial solutions.

---

### **2. Pivot vs Free Variables**
After row-reducing A:

- **Pivot variables** = variables corresponding to pivot columns  
- **Free variables** = variables with no pivots (parameters)

Free variables generate the non-trivial solutions.

---

### **3. Special Solutions**
Each free variable produces one “special solution.”

Example:

If x₂ and x₄ are free variables, you get:
x = s * v₁ + t * v₂


Where v₁ and v₂ are special solution vectors.

---

### **4. Basis for the Nullspace**
The set of special solutions forms a basis for the nullspace N(A).

Nullspace dimension = number of free variables  
= *nullity* of A

---

### **5. Structure**
This lecture is what ties together:

- row reduction
- pivot identification
- free variable count
- general solution structure

…leading into the Four Fundamental Subspaces later.
