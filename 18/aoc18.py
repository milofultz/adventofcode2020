P_IN = "aoc18-data"
P_INS = "aoc18-data-small"


def get_equations(fp):
    with open(fp, 'r') as f:
        data = f.read().replace(' ', '').split('\n')
    return data
    # output = []
    # number = ""
    # for line in data:
    #     for i in range(len(line)):


if __name__ == "__main__":
    equations = get_equations(P_INS)
