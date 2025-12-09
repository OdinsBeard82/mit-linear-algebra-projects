# Lecture 8 – Solving Ax = b: Row Reduced Form (MIT 18.06)

## Core Idea
This lecture extends solving homogeneous systems (Ax = 0) to
**non-homogeneous systems (Ax = b)**.

The key questions:
- Does a solution exist?
- Is the solution unique or are there infinitely many?
- What conditions on b make Ax = b solvable?

---

## Augmented Matrix Approach

To solve Ax = b, we row-reduce the augmented matrix:

[A | b]

If the system reduces to a row like:

0  0  0 | c   (c ≠ 0)

→ the system is **inconsistent** (no solution).

---

## Particular Solution + Nullspace

If a solution exists, the general solution is:

x = x_particular + x_nullspace

- x_particular satisfies Ax = b
- x_nullspace satisfies Ax = 0

This links Lecture 7 (nullspace) directly into Lecture 8.

---

## Geometry Interpretation

- A solution exists **only if b lies in the column space of A**
- If b ∉ C(A), Ax = b has no solution
- Pivot columns still determine the column space

---

## Key Takeaways

- RREF tells you everything about solvability
- Free variables still control infinite solutions
- Column space determines whether b is reachable

