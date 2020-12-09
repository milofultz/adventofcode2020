from collections import deque


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


def is_sum_of_numbers_in_preamble(desired_sum: int, numbers: list) -> bool:
    numbers_hash = set()
    for number in numbers:
        if desired_sum - number in numbers_hash:
            return True
        numbers_hash.add(number)
    return False


def get_encryption_weakness(target: int, numbers: list) -> int:
    for index in range(len(numbers)):
        result = get_contiguous_summands_of_target(target, numbers[:index])
        if result is not None:
            return min(result) + max(result)


def get_contiguous_summands_of_target(target: int, summands: list) -> deque:
    index, contiguous_sum = 0, 0
    contiguous_summands = deque()
    while index < len(summands):
        contiguous_sum = sum(contiguous_summands)
        if contiguous_sum < target:
            contiguous_summands.append(summands[index])
            index += 1
        elif contiguous_sum > target:
            contiguous_summands.popleft()
        else:
            return contiguous_summands


if __name__ == "__main__":
    port_output = get_port_output()
    non_sum_number = get_first_non_sum_number(port_output, 25)
    print(non_sum_number)
    print(get_encryption_weakness(non_sum_number, port_output))
