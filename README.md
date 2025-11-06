
# 🧮 Computor v1

A simple polynomial equation solver.
This project aims to help us reconnect with basic mathematical reasoning by coding a tool that solves polynomial equations of degree 2 or lower.

## 📘 Overview

**Computor** v1 is a command-line program that takes a polynomial equation as input and outputs:

- The **reduced form** of the equation.

- The **polynomial degree**.

- The **solution(s)** depending on the **discriminant** (real or complex).

It accepts equations up to the **second degree**.
Equations of higher degree are detected but **not solved**.

## ⚙️ Usage

### Run
```bash
python3 computorv1.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
```
### Example Outputs
**Example 1 — Second degree**
```bash
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131
```

**Example 2 — First degree**
```bash
python3 computorv1.py "10 * X^0 = 15 * X^0"
Reduced form: -5 * X^0 = 0
No solution.
```

**Example 3 — No solution**
```bash
python3 computorv1.py "10 * X^0 = 15 * X^0"
Reduced form: -5 * X^0 = 0
No solution.
```

**Example 4 — Infinite solutions**
```bash
python3 computorv1.py "6 * X^0 = 6 * X^0"
Reduced form: 0 * X^0 = 0
Any real number is a solution.
```

**Example 5 — Complex solutions**
```bash
python3 computorv1.py "1 * X^0 + 2 * X^1 + 5 * X^2 = 0"
Reduced form: 1 * X^0 + 2 * X^1 + 5 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly negative, the two complex solutions are:
-1/5 + 2i/5
-1/5 - 2i/5
```

## 🧠 Features
- Handles polynomials up to degree 2.

- Simplifies the equation into a reduced form.

- Calculates and displays the discriminant and solutions.

- Detects and reports:

    - No solutions.

    - Infinite solutions.

    - Unsupported degrees (>2).
## 🖥️ Input Format

Each term must respect the structure:

```bash
a * X^p
```
where:

- `a` is a real coefficient (can be positive, negative, or zero),

- `p` is a non-negative integer exponent.

Spaces are optional, but the structure must be respected.

Example of valid input:

```bash
5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
```

## 🧩 Limitations
- Only equations up to second degree are solved.

- Input must strictly follow the `a * X^p` format.

- No advanced math libraries may be used (except for basic arithmetic operations).

## 🚀 Run from Standard Input
If no argument is provided, the program waits for an equation on STDIN:
```bash
$> python3 computorv1.py
Enter equation: 5 * X^0 + 4 * X^1 = 4 * X^0
```

## 💡 Author

### 👨‍💻 ncourtoi

