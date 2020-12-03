PASSWORDS = "aoc02-data"


def main():
    entries = load_data(PASSWORDS).replace(':', '').split('\n')
    valid_entries = get_number_of_valid_entries(entries)
    print(valid_entries)


def load_data(fp):
    with open(fp, 'r') as f:
        data = f.read()
    return data


def get_number_of_valid_entries(entries):
    valid = 0
    for entry in entries:
        amount, char, password = entry.strip().split(' ')
        low, high = amount.split('-')
        if int(low) <= password.count(char) <= int(high):
            valid += 1
    return valid


if __name__ == "__main__":
    main()
