import copy


PUZZLE_INPUT = 'aoc11-data'
EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'
DIRECTIONS = [
    {'x': 0, 'y': -1},  # N
    {'x': 1, 'y': -1},  # NE
    {'x': 1, 'y': 0},   # E
    {'x': 1, 'y': 1},   # SE
    {'x': 0, 'y': 1},   # S
    {'x': -1, 'y': 1},  # SW
    {'x': -1, 'y': 0},  # W
    {'x': -1, 'y': -1}  # NW
]


def get_seat_layout() -> list:
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read().split('\n')
    output = []
    for line in data:
        output.append(list(line))
    return output


def get_settled_layout(layout: list) -> list:
    working_layout = copy.deepcopy(layout)
    last_layout = None
    while last_layout != working_layout:
        last_layout = copy.deepcopy(working_layout)
        for row_number, row in enumerate(last_layout):
            for col_number, seat in enumerate(row):
                if seat == EMPTY and can_be_occupied_adjacent(last_layout, col_number, row_number):
                    working_layout[row_number][col_number] = OCCUPIED
                if seat == OCCUPIED and can_be_emptied_adjacent(last_layout, col_number, row_number):
                    working_layout[row_number][col_number] = EMPTY
    return working_layout


def can_be_occupied_adjacent(layout: list, x: int, y: int) -> bool:
    """ Return True if no occupied seats are adjacent to it """
    x_range, y_range = make_x_y_ranges(x, y, layout)
    for y_offset in y_range:
        for x_offset in x_range:
            if y_offset == 0 and x_offset == 0:
                continue
            if layout[y + y_offset][x + x_offset] == OCCUPIED:
                return False
    return True


def can_be_emptied_adjacent(layout: list, x: int, y: int) -> bool:
    """ Return True if four+ seats adjacent to coordinates are occupied """
    x_range, y_range = make_x_y_ranges(x, y, layout)
    adjacent_occupied_seats = 0
    for y_offset in y_range:
        for x_offset in x_range:
            if y_offset == 0 and x_offset == 0:
                continue
            if layout[y + y_offset][x + x_offset] == OCCUPIED:
                adjacent_occupied_seats += 1
                if adjacent_occupied_seats >= 4:
                    return True
    return False


def make_x_y_ranges(x, y, layout):
    y_range = make_y_range(y, len(layout) - 1)
    x_range = make_x_range(x, len(layout[0]) - 1)
    return x_range, y_range


def make_y_range(y, max_y):
    if y == 0:
        return [0, 1]
    elif y == max_y:
        return [-1, 0]
    else:
        return [-1, 0, 1]


def make_x_range(x, max_x):
    if x == 0:
        return [0, 1]
    elif x == max_x:
        return [-1, 0]
    else:
        return [-1, 0, 1]


def get_occupied_seats(layout: list) -> int:
    occupied_seats = 0
    for row in layout:
        for seat in row:
            if seat == OCCUPIED:
                occupied_seats += 1
    return occupied_seats


def get_settled_layout_from_a_distance(layout: list) -> list:
    working_layout = copy.deepcopy(layout)
    last_layout = None
    while last_layout != working_layout:
        last_layout = copy.deepcopy(working_layout)
        for row_number, row in enumerate(last_layout):
            for col_number, seat in enumerate(row):
                if seat == EMPTY and can_be_occupied_from_a_distance(last_layout, col_number, row_number):
                    working_layout[row_number][col_number] = OCCUPIED
                if seat == OCCUPIED and can_be_emptied_from_a_distance(last_layout, col_number, row_number):
                    working_layout[row_number][col_number] = EMPTY
    return working_layout


def can_be_occupied_from_a_distance(layout: list, x: int, y: int) -> bool:
    """ Return True if no seats visible via directions are occupied """
    for direction in DIRECTIONS:
        x_sight, y_sight = x + direction['x'], y + direction['y']
        width, height = len(layout[0]), len(layout)
        while 0 <= x_sight < width and 0 <= y_sight < height:
            visible_square = layout[y_sight][x_sight]
            if visible_square == OCCUPIED:
                return False
            elif visible_square == EMPTY:
                break
            x_sight += direction['x']
            y_sight += direction['y']
    return True


def can_be_emptied_from_a_distance(layout: list, x: int, y: int) -> bool:
    """ Return True if five or more seats visible via directions are occupied """
    visible_occupied_seats = 0
    for direction in DIRECTIONS:
        x_sight, y_sight = x + direction['x'], y + direction['y']
        width, height = len(layout[0]), len(layout)
        while 0 <= x_sight < width and 0 <= y_sight < height:
            visible_square = layout[y_sight][x_sight]
            if visible_square == OCCUPIED:
                visible_occupied_seats += 1
                if visible_occupied_seats >= 5:
                    return True
                break
            if visible_square == EMPTY:
                break
            x_sight += direction['x']
            y_sight += direction['y']
    return False


if __name__ == "__main__":
    seat_layout = get_seat_layout()
    settled_layout = get_settled_layout(seat_layout)
    print(get_occupied_seats(settled_layout))
    settled_layout_from_a_distance = get_settled_layout_from_a_distance(seat_layout)
    print(get_occupied_seats(settled_layout_from_a_distance))
