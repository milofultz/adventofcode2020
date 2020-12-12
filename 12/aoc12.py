PUZZLE_INPUT = "aoc12-data"
PUZZLE_INPUT_SMALL = "aoc12-data-small"
ARBITRARY = ["N", "S", "W", "E"]
CARDINAL_X_Y = {"N": 1, "S": -1, "W": -1, "E": 1}
DEGREE_X_Y = {0: 1, 90: 1, 180: -1, 270: -1}
ROTATION = ["L", "R"]
ROTATION_POLARITY = {"L": -1, "R": 1}


def get_commands():
    with open (PUZZLE_INPUT, 'r') as f:
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
    if operation in ARBITRARY:
        ship_data["coordinates"] = get_new_coordinates_on_arbitrary_move(command, ship_data["coordinates"])
    elif operation in ROTATION:
        ship_data["direction"] = get_new_direction_on_rotation(command, ship_data)
    else:  # forward
        ship_data = get_ship_data_on_forward_movement(command, ship_data)
    return ship_data


def get_new_coordinates_on_arbitrary_move(command: dict, current_coordinates: tuple) -> tuple:
    direction = command['operation']
    ship_x, ship_y = current_coordinates
    if direction in ["E", "W"]:
        ship_x = ship_x + CARDINAL_X_Y[direction] * command["value"]
    else:
        ship_y = ship_y + CARDINAL_X_Y[direction] * command["value"]
    return ship_x, ship_y


def get_new_direction_on_rotation(command: dict, ship_data: dict) -> int:
    rotation_change = ROTATION_POLARITY[command["operation"]] * command["value"]
    return abs((ship_data["direction"] + rotation_change) % 360)


def get_ship_data_on_forward_movement(command: dict, ship_data: dict) -> dict:
    ship_x, ship_y = ship_data["coordinates"]
    direction = ship_data["direction"]
    distance = command["value"]
    if direction in [90, 270]:
        ship_x = ship_x + distance * DEGREE_X_Y[direction]
    else:  # 0, 180
        ship_y = ship_y + distance * DEGREE_X_Y[direction]
    ship_data["coordinates"] = (ship_x, ship_y)
    return ship_data


def get_manhattan_distance(start: tuple, end: tuple) -> int:
    difference = 0
    difference += abs(start[0] - end[0])
    difference += abs(start[1] - end[1])
    return difference

if __name__ == "__main__":
    commands = get_commands()
    start_coordinates = (0, 0)
    ship_data = {"coordinates": start_coordinates,
                 "direction": 90}  # East
    end_coordinates = get_end_coordinates(commands, ship_data)
    print(get_manhattan_distance(start_coordinates, end_coordinates))
