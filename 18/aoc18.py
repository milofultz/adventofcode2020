import copy


P_IN = "aoc18-data"
P_INS = "aoc18-data-small"
P_INS2 = "aoc18-data-smaller"
OPERATORS = ["+", "*"]


def get_equations(fp):
    with open(fp, 'r') as f:
        data = f.read().replace(' ', '').split('\n')
    output = []
    for line in data:
        output.append(parse_equation(line))
    return output


def parse_equation(raw_eq: str) -> list:
    equation = []
    number = ""
    index = 0
    while index < len(raw_eq):
        if raw_eq[index].isnumeric():
            number += raw_eq[index]
            index += 1
        elif raw_eq[index] in OPERATORS:
            if number != "":
                equation.append(int(number))
            equation.append(raw_eq[index])
            number = ""
            index += 1
        else:
            sub_eq = ""
            parentheses_count = 1
            index += 1
            while parentheses_count != 0:
                if raw_eq[index] == "(":
                    parentheses_count += 1
                elif raw_eq[index] == ")":
                    parentheses_count -= 1
                sub_eq += raw_eq[index] if parentheses_count != 0 else ""
                index += 1
            equation.append(parse_equation(sub_eq))
    if number != "":
        equation.append(int(number))
    return equation


def sum_all_equations(equations: list) -> int:
    total = 0
    for equation in equations:
        total += sum_equation(equation)
    return total


def sum_equation(eq: list) -> int:
    while any(isinstance(element, list) for element in eq):
        for index, element in enumerate(eq):
            if type(element) == list:
                eq[index] = sum_equation(element)
                break

    result = eq[0]
    index = 1
    while index < len(eq):
        if eq[index] == "+":
            result += eq[index + 1]
        else:  # "*"
            result *= eq[index + 1]
        index += 2
    return result


if __name__ == "__main__":
    equations = get_equations(P_IN)
    print(sum_all_equations(equations))
