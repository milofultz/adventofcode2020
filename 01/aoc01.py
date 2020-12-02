def main():
    given_nums = make_list_of_given_nums()
    print(find_two_numbers_sum_of_2020(given_nums))
    print(find_three_numbers_sum_of_2020(given_nums))


def make_list_of_given_nums():
    with open('aoc01-data', 'r') as f:
        data = f.read().split('\n')
    for index, entry in enumerate(data):
        data[index] = int(entry)
    return data


def find_two_numbers_sum_of_2020(numbers: list) -> int:
    for i, num1 in enumerate(numbers):
        for num2 in numbers[i:]:
            if num1 + num2 == 2020:
                return num1 * num2
    return -1


def find_three_numbers_sum_of_2020(numbers: list) -> int:
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers[i:]):
            for num3 in numbers[j:]:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3
    return -1


if __name__ == '__main__':
    main()