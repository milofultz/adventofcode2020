PUZZLE_INPUT = "aoc12-data"
PUZZLE_INPUT_SMALL = "aoc12-data-small"


def get_commands():
    with open (PUZZLE_INPUT, 'r') as f:
        data = f.read().strip().split('\n')
    output = list()
    for line in data:
        command = dict()
        command['operation'] = line[0]
        command['value'] = line[1:].strip()
        output.append(command)
    return output


if __name__ == "__main__":
    commands = get_commands()
    print(commands)
