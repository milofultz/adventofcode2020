from collections import defaultdict


PUZZLE_INPUT = 'aoc10-data'


def get_adapter_list():
    with open(PUZZLE_INPUT, 'r') as f:
        adapter_list = f.read().split('\n')
    adapter_list = sorted([int(adapter) for adapter in adapter_list])
    # Add built in device adapter
    adapter_list.append(adapter_list[-1] + 3)
    return adapter_list


def get_adapter_differences_and_variations(adapters: list) -> (dict, int):
    differences = defaultdict(int)
    variations = defaultdict(int, {0: 1})
    last_adapter = 0
    for adapter in adapters:
        differences[adapter - last_adapter] += 1
        variations[adapter] = variations[adapter - 1] + variations[adapter - 2] + variations[adapter - 3]
        last_adapter = adapter
    return differences, variations


if __name__ == "__main__":
    adapter_list = get_adapter_list()
    difference_dict, variations = get_adapter_differences_and_variations(adapter_list)
    print(difference_dict[1] * difference_dict[3])
    print(variations[adapter_list[-1]])
