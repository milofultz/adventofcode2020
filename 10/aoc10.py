from collections import defaultdict


PUZZLE_INPUT = 'aoc10-data'


def get_adapter_list():
    with open(PUZZLE_INPUT, 'r') as f:
        adapter_list = f.read().split('\n')
    adapter_list = sorted([int(adapter) for adapter in adapter_list])
    # Add built in device adapter
    adapter_list.append(adapter_list[-1] + 3)
    return adapter_list


def get_adapter_differences(adapters: list) -> dict:
    differences = defaultdict(int)
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
    # Part 2