# in: list of numbers
# out: int (# of 1 jolt * # of 3-jolt)

PUZZLE_INPUT = 'aoc10-data'


def get_adapter_list():
    with open(PUZZLE_INPUT, 'r') as f:
        adapter_list = f.read().split('\n')
    return [int(adapter) for adapter in adapter_list]


def get_adapter_differences(adapters: list) -> dict:
    # sort list of adapters
    sorted_adapters = sorted(adapters)
    # create diff dict with 1, 2, and 3 set to 0
    differences = {
        '1': 0,
        '2': 0,
        '3': 1
    }
    # set current adapter to first item in list
    last_adapter = 0
    # for adapter in adapters starting on item 2
    for adapter in sorted_adapters:
        # get diff and increment at key
        difference = adapter - last_adapter
        differences[str(difference)] += 1
        last_adapter = adapter
    # return dict
    return differences


if __name__ == "__main__":
    # get data
    adapter_list = get_adapter_list()
    # get dict of all adapter differences
    difference_dict = get_adapter_differences(adapter_list)
    # return number of 1j * number of 3J
    print(difference_dict['1'] * difference_dict['3'])