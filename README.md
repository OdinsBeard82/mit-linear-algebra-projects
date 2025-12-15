# mit-linear-algebra-projects

Python implementations of **MIT 18.06 Linear Algebra** lectures — building strong mathematical foundations for **AI / Machine Learning**.

---

## Overview

This repository contains Python projects, notes, and mini-implementations based on **MIT OpenCourseWare 18.06 – Linear Algebra**.

Each lecture folder includes:

* **Lecture notes** explaining concepts in plain language
* **Python scripts** implementing the maths step-by-step
* Optional **examples and verification outputs**

The goal is to make linear algebra *understandable, visual, and practical* — not just theoretical.
All work here forms **Phase 1 of a structured 12-month AI / ML study path**.

---

## Lectures Included

| Lecture    | Topic                                      | Status      |
| ---------- | ------------------------------------------ | ----------- |
| Lecture 1  | The Geometry of Linear Equations           | ✅ Completed |
| Lecture 2  | Elimination with Matrices                  | ✅ Completed |
| Lecture 3  | Multiplication and Inverse Matrices        | ✅ Completed |
| Lecture 4  | Factorization into A = LU                  | ✅ Completed |
| Lecture 5  | Transposes, Permutations, Spaces Rⁿ        | ✅ Completed |
| Lecture 6  | Column Space and Nullspace                 | ✅ Completed |
| Lecture 7  | Solving Ax = 0 (Pivot & Special Solutions) | ✅ Completed |
| Lecture 8  | Solving Ax = b (Row-Reduced Form)          | ✅ Completed |
| Lecture 9  | Independence, Basis, and Dimension         | ✅ Completed |
| Lecture 10 | The Four Fundamental Subspaces             | ✅ Completed |

---

## Technologies & Libraries

* **Python**
* **NumPy** – numerical computation
* **SciPy** – matrix factorization and linear algebra routines
* **SymPy** – symbolic math (RREF, nullspaces, bases)
* **Git & GitHub** – version control

---

## Usage

Clone the repository:

```bash
git clone git@github.com:OdinsBeard82/mit-linear-algebra-projects.git
```

Navigate to any lecture folder and run the scripts:

```bash
cd Lecture-4-Factorization-into-LU
python lu_factorization.py
```

Scripts are written to be readable and easy to modify for experimentation.

---

## Requirements

Recommended setup using a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Example `requirements.txt`:**

```
numpy==2.3.4
scipy==1.16.3
sympy==1.14.0
```

---

## Learning Path / AI & ML Roadmap

This repository represents **Phase 1** of a longer learning plan:

1. **Phase 1:** Python + Linear Algebra (this repo) ✅
2. **Phase 2:** Probability & Statistics
3. **Phase 3:** Core Machine Learning (scikit-learn)
4. **Phase 4:** Deep Learning (PyTorch / TensorFlow)
5. **Phase 5:** Deployment & Portfolio Projects

Each phase builds toward practical, production-ready AI systems.

---

## License

MIT License
