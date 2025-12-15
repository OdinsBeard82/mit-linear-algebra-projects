# Lecture 10: The Four Fundamental Subspaces

This lecture ties *everything* together.

Every matrix creates **four spaces**, and understanding how they relate explains
why linear systems behave the way they do.

---

## The Four Subspaces

For a matrix **A**:

1. **Column Space**  
   All possible outputs of `Ax`

2. **Null Space**  
   All vectors `x` where `Ax = 0`

3. **Row Space**  
   Same as the column space of `Aᵀ`

4. **Left Null Space**  
   All vectors `y` where `yᵀA = 0`

---

## Why the Left Null Space Matters

- It explains **redundant equations**
- It shows why some rows disappear in RREF
- It tells us when `Ax = b` is **consistent or impossible**

If `b` is not orthogonal to the left null space → **no solution**

---

## Python Exploration

Using SymPy, I computed the left null space by finding the null space of `Aᵀ`.

This makes the abstract theory very concrete and shows how row dependencies
are detected programmatically.

---

## Big Picture

This lecture completes the foundation for:
- Least squares
- Optimization
- Machine learning loss functions
- Over/underdetermined systems

Everything after this builds on these ideas.
