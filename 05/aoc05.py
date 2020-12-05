PUZZLE_INPUT = 'aoc05-data'


def get_boarding_passes() -> list:
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read()
    return data.split('\n')


def get_highest_seat_id(boarding_passes) -> int:
    highest = 0
    for boarding_pass in boarding_passes:
        seat_id = get_seat_id(boarding_pass)
        if seat_id > highest:
            highest = seat_id
    return highest


def get_seat_id(boarding_pass) -> int:
    row = get_row(boarding_pass[:7])
    column = get_column(boarding_pass[-3:])
    return row * 8 + column


def get_row(directions):
    row_dict = {'F': '0', 'B': '1'}
    row = ''
    for step in directions:
        row += row_dict[step]
    return int(row, 2)


def get_column(directions):
    column_dict = {'L': '0', 'R': '1'}
    column = ''
    for step in directions:
        column += column_dict[step]
    return int(column, 2)


if __name__ == "__main__":
    boarding_passes = get_boarding_passes()
    print(get_highest_seat_id(boarding_passes))