# Lecture 1: Understanding Linear Equations and Their Geometry

## What is a linear equation?
A linear equation is like a balance scale...

## Linear systems
A collection of linear equations with the same unknowns...

## Types of solutions
1. Unique solution
2. No solution
3. Infinitely many solutions

## Solving linear systems with Python

```python
import numpy as np

A = np.array([[2, 1, 0],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])

x = np.linalg.solve(A, b)
print(f"x={x[0]}, y={x[1]}, z={x[2]}")
