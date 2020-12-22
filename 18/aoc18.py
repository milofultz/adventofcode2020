P_IN = "aoc18-data"
P_INS = "aoc18-data-small"
P_INS2 = "aoc18-data-smaller"


def get_equations(fp):
    with open(fp, 'r') as f:
        data = f.read().replace(' ', '').split('\n')
    output = []
    for line in data:
        equation = []
        number = ""
        for char in line:
            if char.isnumeric():
                number += char
            else:
                equation.append(int(number))
                equation.append(char)
                number = ""
        output.append(equation)
    return output


if __name__ == "__main__":
    equations = get_equations(P_INS2)
