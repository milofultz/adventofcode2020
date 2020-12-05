PUZZLE_INPUT = 'aoc05-data'


def main():
    boarding_passes = get_boarding_passes()
    seat_ids = get_all_seat_ids(boarding_passes)
    print(max(seat_ids))
    print(get_missing_seat_id(seat_ids))


def get_boarding_passes() -> list:
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read()
    return data.split('\n')


def get_all_seat_ids(boarding_passes) -> list:
    seat_ids = []
    for boarding_pass in boarding_passes:
        seat_ids.append(get_seat_id(boarding_pass))
    return seat_ids


def get_seat_id(boarding_pass) -> int:
    column, row = get_column_and_row(boarding_pass)
    return row * 8 + column


def get_column_and_row(directions):
    column_dict = {'L': '0', 'R': '1'}
    row_dict = {'F': '0', 'B': '1'}
    column, row = '', ''
    for step in directions:
        if step in column_dict.keys():
            column += column_dict[step]
        else:
            row += row_dict[step]
    return int(column, 2), int(row, 2)


def get_missing_seat_id(seat_ids):
    for i in range(min(*seat_ids, 9), max(*seat_ids, 1015)):
        if i not in seat_ids and i + 1 in seat_ids and i - 1 in seat_ids:
            return i
    return -1


if __name__ == "__main__":
    main()
