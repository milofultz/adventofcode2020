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


def get_end_coordinates(commands: list, ship_data: dict) -> tuple:
    for command in commands:
        ship_data = get_resulting_ship_data_from_command(command, ship_data)
    return ship_data["coordinates"]


def get_resulting_ship_data_from_command(command: dict, ship_data: dict) -> dict:
    return ship_data


if __name__ == "__main__":
    commands = get_commands()
    ship_data = {"coordinates": (0, 0),  # starts at center
                 "direction": 270}       # starts East
    end_coordinates = get_end_coordinates(commands, ship_data)
    print(end_coordinates)
