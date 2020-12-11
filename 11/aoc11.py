import copy


PUZZLE_INPUT = 'aoc11-data'
EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

# ## Parser
#
# IN: Empty layout of seats (string)
# OUT: Parsed seats layout
#
def get_seat_layout() -> list:  # list of lists
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read().split('\n')
    output = []
    for line in data:
        output.append(list(line))
    return output


# ## Program
#
# IN: Parsed seats layout
# OUT: number of occupied seats (int)
#
# Rules:
# - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# - Otherwise, the seat's state does not change.
#
# How to store the seats layout?
# - List of lists
#     - high amount of overhead needed to constantly search the lists
#     - empty seats take up lots of space in list
#     - easy to check adjacent seats
# - hash table with coords as keys
#     - fast search
#     - no empty seats/less space needed
#     - harder to check adjacent seats
#
# Naive solution - List of lists
# FUNC: Get settled seats
# IN: Seat list (list of lists)
# OUT: (modified copy of) Seat list (list of lists)
def get_settled_layout(layout: list) -> list:
    # - make deep copy of seat list to work with
    working_layout = copy.deepcopy(layout)
    # - initial state is None
    last_layout = None
    # - while initial state is not equal to seat list
    while last_layout != working_layout:
    #     - initial state is deep copy of seat list
        last_layout = copy.deepcopy(working_layout)
    #     - For row in seats
        for row_number, row in enumerate(last_layout):
    #         - for each seat in row
            for col_number, seat in enumerate(row):
    #             - if empty and can be occupied (func)
                if seat == EMPTY and can_be_occupied(last_layout, col_number, row_number):
    #                 - set to occupied
                    working_layout[row_number][col_number] = OCCUPIED
    #             - if occupied and can be emptied (func)
                if seat == OCCUPIED and can_be_emptied(last_layout, col_number, row_number):
    #                 - set to empty
                    working_layout[row_number][col_number] = EMPTY
    # - return modified copy of seat list
    return working_layout


# - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
def can_be_occupied(layout: list, x: int, y: int) -> bool:
    x_range = y_range = [-1, 0, 1]
    if y == 0:
        y_range = [0, 1]
    if x == 0:
        x_range = [0, 1]
    if y + 1 == len(layout):
        y_range = [-1, 0]
    if x + 1 == len(layout[0]):
        x_range = [-1, 0]
    for y_offset in y_range:
        for x_offset in x_range:
            if y_offset == 0 and x_offset == 0:
                continue
            if layout[y + y_offset][x + x_offset] == OCCUPIED:
                return False
    return True


# - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
def can_be_emptied(layout: list, x: int, y: int) -> bool:
    adjacent_occupied_seats = 0
    x_range = y_range = [-1, 0, 1]
    if y == 0:
        y_range = [0, 1]
    if x == 0:
        x_range = [0, 1]
    if y + 1 == len(layout):
        y_range = [-1, 0]
    if x + 1 == len(layout[0]):
        x_range = [-1, 0]
    for y_offset in y_range:
        for x_offset in x_range:
            if y_offset == 0 and x_offset == 0:
                continue
            if layout[y + y_offset][x + x_offset] == OCCUPIED:
                adjacent_occupied_seats += 1
                if adjacent_occupied_seats >= 4:
                    return True
    return False


# FUNC: Get occupied seats
# IN: Seat list
# OUT: Occupied seats (int)
#
# - set counter to 0
# - For row in seats
#     - For seat in row
#         - if seat is occupied
#             - counter += 1
# - return counter
def get_occupied_seats(layout: list) -> int:
    occupied_seats = 0
    for row in layout:
        for seat in row:
            if seat == OCCUPIED:
                occupied_seats += 1
    return occupied_seats


if __name__ == "__main__":
    seat_layout = get_seat_layout()
    settled_layout = get_settled_layout(seat_layout)
    print(get_occupied_seats(settled_layout))