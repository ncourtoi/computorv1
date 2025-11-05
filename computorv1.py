import sys
import re

term_pattern = re.compile(r'([+-]?\d*\.?\d*)\*X\^(\d+)')

def my_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def my_sqrt(x, epsilon=1e-10):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number.")
    if x == 0:
        return 0.0
    guess = x
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess

def parse_side(side_str, side_label):
    tokens = []
    for match in term_pattern.finditer(side_str):
        coef = match.group(1)
        power = int(match.group(2))
        if coef in ["", "+"]:
            coef = 1.0
        elif coef == "-":
            coef = -1.0
        else:
            coef = float(coef)
        tokens.append({"coef": coef, "power": power, "side": side_label})
    return tokens


def solve_posdelta(reduced, delta):
    a = int(reduced.get(2, 0))
    b = int(reduced.get(1, 0))
    delta_abs = abs(delta)

    real_num = -b
    imag_num = int(my_sqrt(delta_abs))
    denom = 2 * a

    real_gcd = my_gcd(abs(real_num), abs(denom))
    real_num_reduced = real_num // real_gcd
    real_denom_reduced = denom // real_gcd

    imag_gcd = my_gcd(imag_num, abs(denom))
    imag_num_reduced = imag_num // imag_gcd
    imag_denom_reduced = denom // imag_gcd

    print("Discriminant is strictly negative, the two complex solutions are:")
    print(f"{real_num_reduced}/{real_denom_reduced} + {imag_num_reduced}i/{imag_denom_reduced}")
    print(f"{real_num_reduced}/{real_denom_reduced} - {imag_num_reduced}i/{imag_denom_reduced}")

def print_reduced(reduced):
    terms = []

    reduced = {p: c for p, c in reduced.items()}
    for power in sorted(reduced.keys()):
        coef = reduced[power]
        sign = "+" if coef >= 0 and terms else ""
        terms.append(f"{sign} {coef} * X^{power}")
    print(f"Reduced form: {' '.join(terms)} = 0")

def reduce_equation(tokens):
    reduced = {}
    for term in tokens:
        coef = term["coef"]
        power = term["power"]
        if term["side"] == "right":
            coef = -coef
        reduced[power] = reduced.get(power, 0) + coef

    print_reduced(reduced)

    if (reduced.__len__() == 1 and reduced.get(0) == 0):
        reduced = {p: c for p, c in reduced.items()}
    else:
        reduced = {p: c for p, c in reduced.items() if abs(c) > 1e-12}

    degree = max(reduced.keys(), default=0)
    print(f"Polynomial degree: {degree}")

    return reduced, degree


def solve_equation(reduced, degree):
    if degree == 0:
        if len(reduced) == 0 or reduced.get(0, 0) == 0:
            print("Any real number is a solution")
        else:
            print("No solution")


    elif degree == 1:
        if (reduced.get(0) == None):
            print("The solution is: 0")
            return
        X = -(reduced.get(0) / reduced.get(1, 0))
        print(f"The Solution is:\n{X}")

    elif degree == 2:
        delta = reduced.get(1, 0) ** 2 - 4 * reduced.get(2, 0) * reduced.get(0, 0)

        if delta > 0:
            print("Discriminant is strictly positive, the two solutions are:")
            X1 = (-reduced.get(1) - my_sqrt(delta)) / (2 * reduced.get(2))
            X2 = (-reduced.get(1) + my_sqrt(delta)) / (2 * reduced.get(2))
            print(f"{X1}\n{X2}")

        elif delta < 0:
            solve_posdelta(reduced, delta)
        elif delta == 0:
            X = -reduced.get(1) / (2 * reduced.get(2))
            print(f"The solution is:\n{X}")

    else:
        print("The polynomial degree is strictly greater than 2, I can't solve.")


def main():
    if len(sys.argv) < 2:
        equation = input("Enter the equation to resolve: ")
    elif len(sys.argv) == 2:
        equation = sys.argv[1]
    else:
        print("Too much arguments")
        sys.exit()

    try:
        equation = equation.replace(" ", "")
        left, right = equation.split("=")
        tokens = parse_side(left, "left") + parse_side(right, "right")
        reduced, degree = reduce_equation(tokens)
        solve_equation(reduced, degree)
    except Exception as e:
        print("Error", e)


if __name__ == "__main__":
    main()
