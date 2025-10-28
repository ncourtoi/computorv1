import sys
import re
from math import *

term_pattern = re.compile(r'([+-]?\d*\.?\d*)\*X\^(\d+)')
def parse_side(side_str, side_label):
    tokens = []
    for match in term_pattern.finditer(side_str):
        coef = match.group(1)
        power = int(match.group(2))
        coef = float(coef) if coef not in ["", "+", "-"] else float(coef + "1") if coef in ["+", "-"] else 1.0
        tokens.append({"coef": coef, "power": power, "side": side_label})
    return tokens

def reduce_equation(tokens):
    reduced = {}
    for term in tokens:
        coef = term["coef"]
        power = term["power"]
        if term["side"] == "right":
            coef = -coef
        reduced[power] = reduced.get(power, 0) + coef
    print(f"Brut Form Before: {reduced}")
    if (reduced.__len__() == 1 and reduced.get(0) == 0):
        reduced = {p: c for p, c in reduced.items()}
    else:
        reduced = {p: c for p, c in reduced.items() if abs(c) > 1e-12}
    print(f"Brut Form After: {reduced}")
    terms = []
    for power in sorted(reduced.keys()):
        coef = reduced[power]
        sign = "+" if coef >= 0 and terms else ""
        terms.append(f"{sign} {coef} * X^{power}")
    reduced_str = " ".join(terms)
    print(f"Reduced form: {reduced_str} = 0")

    degree = max(reduced.keys(), default=0)
    print(f"Polynomial degree: {degree}")

    return reduced, degree

def solve_equation(reduced, degree):
    if degree == 0:
        if reduced.keys() == 0:
            print("Any real number is a solution")
        else:
            print("No solution")
    elif degree == 1:
        X = -(reduced.get(0) / reduced.get(1))
        print(f"The Solution is:\n{X}")
    elif degree == 2:
        delta = reduced.get(1) ** 2 - 4 * reduced.get(2) * reduced.get(0)
        print(delta)
        if (delta > 0):
            print("Discriminant is strictly positive, the two solutions are:")
            X1 = (-reduced.get(1) - sqrt(delta)) / (2 * reduced.get(2))
            X2 = (-reduced.get(1) + sqrt(delta)) / (2 * reduced.get(2))
            print(f"{X1}\n {X2}")
        if (delta < 0):
            print("Discriminant is strictly negative, the two complex solutions are:")
            print(f"{-reduced.get(1)}{-sqrt(delta)}")
        else:
            X = -reduced.get(1) / (2 * reduced.get(2))
            print(f"The solution is:\n{X}")
    print("The polynomial degree is strictly greater than 2, I can't solve.")

def main():
    if (len(sys.argv) < 2):
        equation = (input("Enter the equation to resolve: "))
    elif(len(sys.argv) == 2):
        equation = sys.argv[1]
    else:
        print("Too much arguments")
        sys.exit()
    try:
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        tokens = parse_side(left, "left") + parse_side(right, "right")
        #print(f"Parsed equation: {tokens}")
        reduced, degree = reduce_equation(tokens)
        solve_equation(reduced, degree)
    except Exception as e:
        print("Error", e)

if __name__ == "__main__":
    main()