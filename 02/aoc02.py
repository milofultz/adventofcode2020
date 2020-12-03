PASSWORDS = "aoc02-data"


def main():
    entries = load_data(PASSWORDS).replace(':', '').split('\n')
    count_valid, index_valid = get_valid_entries(entries)
    print(f"Part 1: {count_valid}\n" +
          f"Part 2: {index_valid}")


def load_data(fp):
    with open(fp, 'r') as f:
        data = f.read()
    return data


def get_valid_entries(entries):
    count_valid, index_valid = 0, 0
    for entry in entries:
        amount, char, password = entry.split(' ')
        low, high = amount.split('-')
        low, high = int(low), int(high)
        if low <= password.count(char) <= high:
            count_valid += 1
        if (password[low-1] == char) ^ (password[high-1] == char):
            index_valid += 1
    return count_valid, index_valid


if __name__ == "__main__":
    main()
