PASSWORDS = "aoc02-data"


def main():
    entries = load_data(PASSWORDS).replace(':', '').split('\n')
    print(get_valid_entries_using_char_count(entries))


def load_data(fp):
    with open(fp, 'r') as f:
        data = f.read()
    return data


def get_valid_entries_using_char_count(entries):
    valid = 0
    for entry in entries:
        amount, char, password = entry.strip().split(' ')
        low, high = amount.split('-')
        if int(low) <= password.count(char) <= int(high):
            valid += 1
    return valid


if __name__ == "__main__":
    main()
