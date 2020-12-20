PUZZLE_INPUT = 'aoc10-data'


def get_adapter_list():
    with open(PUZZLE_INPUT, 'r') as f:
        adapter_list = f.read().split('\n')
    return sorted([int(adapter) for adapter in adapter_list])


def get_adapter_differences(adapters: list) -> dict:
    differences = {1: 0, 2: 0, 3: 1}
    last_adapter = 0
    for adapter in adapters:
        differences[adapter - last_adapter] += 1
        last_adapter = adapter
    return differences


if __name__ == "__main__":
    adapter_list = get_adapter_list()
    # Part 1
    difference_dict = get_adapter_differences(adapter_list)
    print(difference_dict[1] * difference_dict[3])
