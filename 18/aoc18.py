import copy


P_IN = "aoc18-data"
P_INS = "aoc18-data-small"
P_INS2 = "aoc18-data-smaller"
OPERATORS = ["+", "*"]


def get_equations(fp):
    with open(fp, 'r') as f:
        data = f.read().replace(' ', '').split('\n')
    return [parse_equation(line) for line in data]


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
            parentheses_depth = 1
            index += 1
            while parentheses_depth != 0:
                if raw_eq[index] == "(":
                    parentheses_depth += 1
                elif raw_eq[index] == ")":
                    parentheses_depth -= 1
                sub_eq += raw_eq[index] if parentheses_depth != 0 else ""
                index += 1
            equation.append(parse_equation(sub_eq))
    if number != "":
        equation.append(int(number))
    return equation


def sum_all_equations(equations: list) -> tuple:
    total_no_precedence = 0
    total_add_precedence = 0
    for equation in equations:
        total_no_precedence += sum_equation(equation)
        total_add_precedence += sum_equation(equation, True)
    return total_no_precedence, total_add_precedence


def sum_equation(eq: list, plus_precedence: bool = False) -> int:
    def flatten_equation(nested_eq: list) -> list:
        flattened_eq = copy.deepcopy(nested_eq)
        for i, element in enumerate(flattened_eq):
            if type(element) == list:
                flattened_eq[i] = sum_equation(element, plus_precedence)
        return flattened_eq

    eq = flatten_equation(eq)
    while "+" in eq and plus_precedence:
        plus_i = eq.index("+")
        eq[plus_i - 1] = eq[plus_i - 1] + eq[plus_i + 1]
        del eq[plus_i:plus_i + 2]
    result = eq[0]
    operator_i = 1
    while operator_i < len(eq):
        if eq[operator_i] == "*":
            result *= eq[operator_i + 1]
        else:  # "+"
            result += eq[operator_i + 1]
        operator_i += 2
    return result


if __name__ == "__main__":
    equations = get_equations(P_IN)
    print(sum_all_equations(equations))
