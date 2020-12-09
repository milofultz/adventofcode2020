PUZZLE_INPUT = 'aoc09-data'


def get_port_output() -> list:
    with open(PUZZLE_INPUT, 'r') as f:
        output = f.read().split('\n')
    return [int(line) for line in output]


def get_first_non_sum_number(numbers: list, size_of_preamble: int) -> int:
    start, current_index = 0, size_of_preamble
    for number in numbers[size_of_preamble:]:
        if not is_sum_of_numbers_in_preamble(number, numbers[start:current_index]):
            return number
        start += 1
        current_index += 1
    return None


def is_sum_of_numbers_in_preamble(desired_sum, numbers):
    for index, first_num in enumerate(numbers):
        for second_num in numbers[index + 1:]:
            if first_num + second_num == desired_sum:
                return True
    return False


def get_encryption_weakness(target: int, numbers: list) -> int:
    for index in range(len(numbers)):
        result = get_contiguous_summands_of_target(target, numbers[:index])
        if result is not None:
            return min(result) + max(result)
    return None


def get_contiguous_summands_of_target(target: int, summands: list) -> list:
    if len(summands) < 2:
        return None
    for first_number_index, first_number in enumerate(summands):
        if first_number > target:
            continue
        contiguous_sum = first_number
        contiguous_summands = [first_number]
        second_number_index = first_number_index + 1
        for second_number in summands[second_number_index:]:
            contiguous_sum += second_number
            contiguous_summands.append(second_number)
            if contiguous_sum > target:
                break
            elif contiguous_sum == target:
                return contiguous_summands
    return None


if __name__ == "__main__":
    port_output = get_port_output()
    non_sum_number = get_first_non_sum_number(port_output, 25)
    print(non_sum_number)
    print(get_encryption_weakness(non_sum_number, port_output))
