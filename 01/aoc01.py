def main():
    given_nums = make_list_of_given_nums()
    print(find_products_of_sums_of_2020(given_nums))


def make_list_of_given_nums():
    with open('aoc01-data', 'r') as f:
        data = f.read().split('\n')
    for index, entry in enumerate(data):
        data[index] = int(entry)
    return data


def find_products_of_sums_of_2020(numbers: list) -> int:
    two, three = 0, 0
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers[i:]):
            if num1 + num2 == 2020:
                two = num1 * num2
            for num3 in numbers[j:]:
                if num1 + num2 + num3 == 2020:
                    three = num1 * num2 * num3
    return two, three


if __name__ == '__main__':
    main()