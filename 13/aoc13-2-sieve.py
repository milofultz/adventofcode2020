"""
Got this answer from Gravitar64's post on Reddit.
https://www.reddit.com/r/adventofcode/comments/kc4njx/comment/gfqeouq
"""


PUZZLE_INPUT = "aoc13-data"
PUZZLE_INPUT_SMALL = "aoc13-data-small"


def get_offset_and_ids() -> list:
    with open(PUZZLE_INPUT, "r") as f:
        ids = f.read().strip().split("\n")[1].split(',')
    return [(offset, int(bus_id))
            for offset, bus_id in enumerate(ids)
            if bus_id.isnumeric()]


def get_first_bus_departure_time(bus_ids: list) -> int:
    # set departure time of first bus to 0
    time_of_first_bus = 0
    # set least common multiple to 1, the base case if no numbers given
    least_common_multiple = 1
    # for each time offset and current bus ID in the bus ID list:
    for offset, current_bus_id in bus_ids:
        # while the remainder of the departure time of the first bus plus the
        # offset all divided by the current bus ID doesn't equal zero
        while (time_of_first_bus + offset) % current_bus_id != 0:
            # add the least common multiple to the departure time
            time_of_first_bus += least_common_multiple
        # set the least common multiple to the current bus ID times itself (this
        # works because all the numbers are prime!)
        least_common_multiple *= current_bus_id
    # return the departure time of the first bus
    return time_of_first_bus


if __name__ == "__main__":
    bus_ids = get_offset_and_ids()
    # print(bus_ids)
    print(get_first_bus_departure_time(bus_ids))