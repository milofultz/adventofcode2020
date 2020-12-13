PUZZLE_INPUT = "aoc13-data"
PUZZLE_INPUT_SMALL = "aoc13-data-small"


def get_offset_and_ids():
    with open(PUZZLE_INPUT_SMALL, "r") as f:
        ids = f.read().strip().split("\n")[1].split(',')
    return [(offset, int(bus_id))
            for offset, bus_id in enumerate(ids)
            if bus_id.isnumeric()]


if __name__ == "__main__":
    bus_ids = get_offset_and_ids()
    print(bus_ids)
