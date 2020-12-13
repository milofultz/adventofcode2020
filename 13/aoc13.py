PUZZLE_INPUT = "aoc13-data"
PUZZLE_INPUT_SMALL = "aoc13-data-small"


def get_arrival_time_and_ids():
    with open(PUZZLE_INPUT_SMALL, "r") as f:
        arrival, ids = f.read().split("\n")
    return int(arrival), [int(bus_id) for bus_id in ids.split(",") if bus_id != "x"]


if __name__ == "__main__":
    arrival, bus_ids = get_arrival_time_and_ids()
    print(arrival, bus_ids)
