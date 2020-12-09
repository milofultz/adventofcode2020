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


if __name__ == "__main__":
    data = get_data()
    print(get_first_non_sum_number(data, 25))
