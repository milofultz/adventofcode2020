PUZZLE_INPUT = "aoc12-data"
PUZZLE_INPUT_SMALL = "aoc12-data-small"
CARDINAL_TO_DEGREES = {"N": 0, "E": 90, "S": 180, "W": 270}
DEGREES_TO_CARDINAL = {0: "N", 90: "E", 180: "S", 270: "W"}
CARDINAL_X_Y = {"N": 1, "E": 1, "S": -1, "W": -1}
ROTATION = ["L", "R"]
ROTATION_POLARITY = {"L": -1, "R": 1}


def get_commands():
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read().strip().split('\n')
    output = list()
    for line in data:
        command = dict()
        command["operation"] = line[0]
        command["value"] = int(line[1:].strip())
        output.append(command)
    return output


def get_end_coordinates(commands: list, ship_data: dict) -> tuple:
    for command in commands:
        ship_data = get_resulting_ship_data_from_command(command, ship_data)
    return ship_data["coordinates"]


def get_resulting_ship_data_from_command(command: dict, ship_data: dict) -> dict:
    operation, value = command["operation"], command["value"]
    if operation in ROTATION:
        ship_data["direction"] = get_new_direction_on_rotation(command, ship_data)
    else:
        direction = ship_data["direction"] if operation == "F" else operation
        ship_data["coordinates"] = get_coordinates_on_movement(direction, value, ship_data["coordinates"])
    return ship_data


def get_new_direction_on_rotation(command: dict, ship_data: dict) -> str:
    rotation_direction, degrees = command["operation"], command["value"]
    ship_direction = CARDINAL_TO_DEGREES[ship_data["direction"]]
    rotation_change = ROTATION_POLARITY[rotation_direction] * degrees
    new_direction = abs((ship_direction + rotation_change) % 360)
    return DEGREES_TO_CARDINAL[new_direction]


def get_coordinates_on_movement(direction: str, distance: int, coordinates: dict) -> tuple:
    ship_x, ship_y = coordinates
    if direction in ["E", "W"]:
        ship_x = ship_x + distance * CARDINAL_X_Y[direction]
    else:  # N, S
        ship_y = ship_y + distance * CARDINAL_X_Y[direction]
    return ship_x, ship_y


def get_manhattan_distance(start: tuple, end: tuple) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


if __name__ == "__main__":
    commands = get_commands()
    start_coordinates = (0, 0)
    ship_data = {"coordinates": start_coordinates, "direction": "E"}
    end_coordinates = get_end_coordinates(commands, ship_data)
    print(get_manhattan_distance(start_coordinates, end_coordinates))
