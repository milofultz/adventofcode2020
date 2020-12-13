PUZZLE_INPUT = "aoc13-data"
PUZZLE_INPUT_SMALL = "aoc13-data-small"


def get_ids():
    with open(PUZZLE_INPUT_SMALL, "r") as f:
        bus_ids = f.read().strip().split("\n")[1].split(",")
    for index, bus_id in enumerate(bus_ids):
        bus_ids[index] = int(bus_id) if bus_id.isnumeric() else bus_id
    return bus_ids


def get_timestamp_of_departing_buses(bus_ids: list) -> int:
    largest = max(bus for bus in bus_ids if type(bus) == int)
    largest_offset = bus_ids.index(largest)
    multiple = 1
    found = False
    while not found:
        found = True
        target = multiple * largest
        for index, num in enumerate(bus_ids):
            offset = index - largest_offset
            # print(target, num, index)
            if num == largest or num == "x":
                continue
            elif (target + offset) % num != 0:
                found = False
                break
        multiple += 1
    return target


if __name__ == "__main__":
    bus_ids = get_ids()
    # print(bus_ids)
    print(get_timestamp_of_departing_buses(bus_ids))
