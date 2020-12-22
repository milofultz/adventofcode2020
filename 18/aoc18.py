P_IN = "aoc18-data"
P_INS = "aoc18-data-small"
P_INS2 = "aoc18-data-smaller"


def get_equations(fp):
    with open(fp, 'r') as f:
        data = f.read().replace(' ', '').split('\n')
    output = []
    for line in data:
        output.append(parse_equation(line))
    return output


def parse_equation(raw_eq):
    equation = []
    number = ""
    index = 0
    while index < len(raw_eq):
        if raw_eq[index].isnumeric():
            number += raw_eq[index]
        elif raw_eq[index] in ["+", "*"]:
            equation.append(int(number))
            equation.append(raw_eq[index])
            number = ""
        elif raw_eq[index] == "(":
            sub_eq = ""
            parentheses_count = 1
            index += 1
            while parentheses_count != 0:
                print(raw_eq[index])
                if raw_eq[index] == "(":
                    parentheses_count += 1
                elif raw_eq[index] == ")":
                    parentheses_count -= 1
                sub_eq += raw_eq[index] if parentheses_count != 0 else ""
                index += 1
            equation.append(parse_equation(sub_eq))
        index += 1
    equation.append(number)
    return equation


if __name__ == "__main__":
    equations = get_equations(P_INS2)
    print(equations)
