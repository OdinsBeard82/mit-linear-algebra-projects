# Lecture 9: Independence, Basis, and Dimension (MIT 18.06)

## Linear Independence

A set of vectors is **linearly independent** if the only solution to:

Ax = 0

is the trivial solution.

If one vector can be written as a combination of others, the set is
**linearly dependent**.

---

## Basis

A **basis** for a vector space is:
- A set of linearly independent vectors
- That spans the space

Every vector in the space can be written uniquely as a linear combination of
basis vectors.

---

## Dimension

The **dimension** of a vector space is the number of vectors in any basis
for that space.

Key results:
- Dimension = rank of the matrix
- Dimension = number of pivot columns
- Free variables do **not** contribute to dimension

---

## Connection to Previous Lectures

- Pivot columns → basis for column space
- Special solutions → basis for nullspace
- Rank–Nullity links dimension across spaces

This lecture ties together:
- elimination
- nullspace
- column space
- rank

---

## Key Takeaway

Everything in linear algebra reduces to:
- independence
- spanning
- dimension

These ideas show up constantly in machine learning and data science.

