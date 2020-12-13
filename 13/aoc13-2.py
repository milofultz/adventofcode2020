PUZZLE_INPUT = "aoc13-data"
PUZZLE_INPUT_SMALL = "aoc13-data-small"


def get_ids():
    with open(PUZZLE_INPUT_SMALL, "r") as f:
        bus_ids = f.read().strip().split("\n")[1].split(",")
    for index, bus_id in enumerate(bus_ids):
        bus_ids[index] = int(bus_id) if bus_id.isnumeric() else bus_id
    return bus_ids


if __name__ == "__main__":
    bus_ids = get_ids()
    print(bus_ids)
