PUZZLE_INPUT = 'aoc10-data'


def get_adapter_list():
    with open(PUZZLE_INPUT, 'r') as f:
        adapter_list = f.read().split('\n')
    adapter_list = sorted([int(adapter) for adapter in adapter_list])
    # Add built in device adapter
    adapter_list.append(adapter_list[-1] + 3)
    return adapter_list


def get_adapter_differences(adapters: list) -> dict:
    differences = {1: 0, 2: 0, 3: 0}
    last_adapter = 0
    for adapter in adapters:
        differences[adapter - last_adapter] += 1
        last_adapter = adapter
    return differences


def get_adapter_variations(adapters: list) -> int:
    # - set total to 0
    total = 0
    # -- base case
    # - if length of adapter array is 1, return 1
    if len(adapters) == 1:
        return 1
    # -- recursive case
    # - else:
    else:
        # - first array element is start
        first = adapters[0]
        # - for each index, adapter in list:
        for i, adapter in enumerate(adapters[1:]):
            if first < adapter <= first + 3:
                # - sum += func([start] + array[index:])
                total += get_adapter_variations(adapters[i+1:])
        # - return total
        if total > 1000000:
            print(total)
        return total


if __name__ == "__main__":
    adapter_list = get_adapter_list()
    # Part 1
    difference_dict = get_adapter_differences(adapter_list)
    print(difference_dict[1] * difference_dict[3])
    # Part 2
    print(get_adapter_variations(adapter_list))