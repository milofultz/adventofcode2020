PUZZLE_INPUT = "aoc13-data"
PUZZLE_INPUT_SMALL = "aoc13-data-small"


def get_arrival_time_and_ids():
    with open(PUZZLE_INPUT_SMALL, "r") as f:
        arrival, ids = f.read().split("\n")
    return int(arrival), [int(bus_id) for bus_id in ids.split(",") if bus_id != "x"]


def part_1_solution(arrival: int, bus_ids: list) -> int:
    earliest_bus = get_earliest_bus_info(arrival, bus_ids)
    print(earliest_bus)
    return earliest_bus["id"] * earliest_bus["wait"]


def get_earliest_bus_info(arrival: int, bus_ids: list) -> dict:
    earliest_bus = {"id": 0, "time": 1e10, "wait": 1e10}
    for bus_id in bus_ids:
        prev_bus_time, minutes_before = divmod(arrival, bus_id)
        this_bus = {"id": bus_id,
                    "time": (prev_bus_time + 1) * bus_id,
                    "wait": bus_id - minutes_before}
        print(bus_id, this_bus)
        if this_bus["wait"] < earliest_bus["wait"]:
            earliest_bus = this_bus
    return earliest_bus


if __name__ == "__main__":
    arrival, bus_ids = get_arrival_time_and_ids()
    # print(arrival, bus_ids)
    print(part_1_solution(arrival, bus_ids))
