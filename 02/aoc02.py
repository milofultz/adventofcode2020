import re


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
        amount, char, password = entry.replace('-', ',').split(' ')
        pattern = re.compile(char + "{" + amount + "}")
        if pattern.search(password):
            valid += 1
    return valid


# Print all results on page
#   If failed, ❌ in red with why
#   If correct, ✅ in green with why


if __name__ == "__main__":
    main()
