import copy
from typing import Callable


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


def sum_all_equations(equations: list) -> tuple:
    total_no_precedence = 0
    total_add_precedence = 0
    for equation in equations:
        total_no_precedence += sum_equation_no_precedence(equation)
        total_add_precedence += sum_equation_add_precedence(equation)
    return total_no_precedence, total_add_precedence


def flatten_equation(nested_eq: list, callback: Callable[[list], int]) -> list:
    flattened_eq = copy.deepcopy(nested_eq)
    for index, element in enumerate(flattened_eq):
        if type(element) == list:
            flattened_eq[index] = callback(element)
    return flattened_eq


def sum_equation_no_precedence(eq: list) -> int:
    while any(isinstance(element, list) for element in eq):
        eq = flatten_equation(eq, sum_equation_no_precedence)
    result = eq[0]
    index = 1
    while index < len(eq):
        if eq[index] == "+":
            result += eq[index + 1]
        else:  # "*"
            result *= eq[index + 1]
        index += 2
    return result


def sum_equation_add_precedence(eq: list) -> int:
    while any(isinstance(element, list) for element in eq):
        eq = flatten_equation(eq, sum_equation_add_precedence)
    while "+" in eq:
        index = eq.index("+")
        eq[index - 1] = eq[index - 1] + eq[index + 1]
        del eq[index:index + 2]
    result = eq[0]
    index = 1
    while index < len(eq):
        result *= eq[index + 1]
        index += 2
    return result


if __name__ == "__main__":
    equations = get_equations(P_IN)
    print(sum_all_equations(equations))
