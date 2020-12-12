PUZZLE_INPUT = "aoc12-data"
PUZZLE_INPUT_SMALL = "aoc12-data-small"
CARDINAL_TO_DEGREES = {"N": 0, "E": 90, "S": 180, "W": 270}
DEGREES_TO_CARDINAL = {0: "N", 90: "E", 180: "S", 270: "W"}
CARDINAL_POLARITY = {"N": 1, "E": 1, "S": -1, "W": -1}
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
        ship_x = ship_x + distance * CARDINAL_POLARITY[direction]
    else:  # N, S
        ship_y = ship_y + distance * CARDINAL_POLARITY[direction]
    return ship_x, ship_y


def get_manhattan_distance(start: tuple, end: tuple) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def get_end_coordinates_with_waypoint(commands: list, ship_coordinates: tuple) -> tuple:
    waypoint_coordinates = (10, 1)  # starts 10E, 1N
    for command in commands:
        if command["operation"] == "F":
            ship_coordinates = get_ship_coordinates_after_command_via_waypoint(
                command["value"], ship_coordinates, waypoint_coordinates)
        else:
            waypoint_coordinates = get_waypoint_coordinates_from_command(command, waypoint_coordinates)
    return ship_coordinates


def get_ship_coordinates_after_command_via_waypoint(
        num: int, ship_coordinates: tuple, waypoint_coordinates: tuple) -> tuple:
    x_to_travel = waypoint_coordinates[0] * num
    y_to_travel = waypoint_coordinates[1] * num
    return ship_coordinates[0] + x_to_travel, ship_coordinates[1] + y_to_travel


def get_waypoint_coordinates_from_command(command: dict, waypoint_coordinates: tuple) -> tuple:
    if command["operation"] in ["N", "S", "E", "W"]:
        return get_moved_waypoint_coordinates(waypoint_coordinates, command)
    else:  # L, R
        return get_rotated_waypoint_coordinates(command, waypoint_coordinates)


def get_moved_waypoint_coordinates(waypoint_coordinates: tuple, command: dict) -> tuple:
    direction = command["operation"]
    if direction in ["N", "S"]:
        new_y = waypoint_coordinates[1] + CARDINAL_POLARITY[direction] * command["value"]
        return waypoint_coordinates[0], new_y
    else:  # E, W
        new_x = waypoint_coordinates[0] + CARDINAL_POLARITY[direction] * command["value"]
        return new_x, waypoint_coordinates[1]


def get_rotated_waypoint_coordinates(command: dict, waypoint_coordinates: tuple) -> tuple:
    if command["operation"] == "L":
        turns = command["value"] // 90
    else:
        turns = 360 - command["value"] // 90
    current_x, current_y = waypoint_coordinates
    for turn in range(turns):
        old_x, old_y = current_x, current_y
        current_x, current_y = -old_y, old_x
    return current_x, current_y


if __name__ == "__main__":
    commands = get_commands()
    start_coordinates = (0, 0)
    ship_data = {"coordinates": start_coordinates, "direction": "E"}

    # Part 1
    end_coordinates = get_end_coordinates(commands, ship_data)
    print(get_manhattan_distance(start_coordinates, end_coordinates))

    # Part 2
    end_coordinates = get_end_coordinates_with_waypoint(commands, start_coordinates)
    print(get_manhattan_distance(start_coordinates, end_coordinates))
