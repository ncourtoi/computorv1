import sys
import re

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
    print("reduced")

#def resolve_equation(equation):

#def identify_degree(equation):




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
        tokens = parse_side(left, "left"), parse_side(right, "right")
        print(equation)
        print(tokens)
    except:
        print("Error")

if __name__ == "__main__":
    main()