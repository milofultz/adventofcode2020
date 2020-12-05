PUZZLE_INPUT = 'aoc04-data'


def main():
    passports = get_passports()
    print(get_number_of_valid_passports(passports))


def get_passports():
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read()
    return parse_passports_from_data(data)


def parse_passports_from_data(data: str) -> list:
    raw_passports = data.split('\n\n')
    passports = []
    for line in raw_passports:
        passports.append(parse_fields_from_string(line))
    return passports


def parse_fields_from_string(line: str) -> dict:
    entry = line.replace('\n', ' ')
    raw_fields = [field.strip() for field in entry.split()]
    parsed_fields = dict()
    for field in raw_fields:
        key, value = field.split(':')
        parsed_fields[key] = value
    return parsed_fields


def get_number_of_valid_passports(passports):
    valid_count = 0
    for passport in passports:
        if has_required_fields(passport):
            valid_count += 1
    return valid_count


def has_required_fields(obj) -> bool:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in required_fields:
        if key not in obj.keys():
            return False
    return True


if __name__ == "__main__":
    main()
