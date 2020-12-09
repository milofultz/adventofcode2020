PUZZLE_INPUT = 'aoc09-data'


def get_data():
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read().split('\n')
    return [int(num) for num in data]


def get_first_non_sum_number(numbers: list, size_of_components: int) -> int:
    start, current_index = 0, size_of_components
    for number in numbers[size_of_components:]:
        if not is_sum_of_components(number, numbers[start:current_index]):
            return number
        start += 1
        current_index += 1
    return None


def is_sum_of_components(desired_sum, components):
    for start, first_num in enumerate(components):
        for second_num in components[start + 1:]:
            if first_num + second_num == desired_sum:
                return True
    return False


def get_encryption_weakness(target: int, numbers: list) -> int:
    for index in range(2, len(numbers)):
        result = get_contiguous_summands_of_target(target, numbers[:index])
        if result is not None:
            return min(result) + max(result)
    return None


def get_contiguous_summands_of_target(target: int, summands: list) -> list:
    for start, first_number in enumerate(summands):
        resulting_summands = [first_number]
        too_big = False
        for second_number in summands[start+1:]:
            if not too_big:
                resulting_summands.append(second_number)
                temp_sum = sum(resulting_summands)
                if temp_sum == target:
                    return resulting_summands
                elif temp_sum > target:
                    too_big = True
    return None


if __name__ == "__main__":
    data = get_data()
    target = get_first_non_sum_number(data, 25)
    print(target)
    print(get_encryption_weakness(target, data))