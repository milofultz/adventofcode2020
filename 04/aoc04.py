PUZZLE_INPUT = 'aoc04-data'

def get_passports():
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read().split('\n\n')
    passports = []
    for raw_passport in data:
        entry = raw_passport.replace('\n', ' ')
        fields = [field.strip() for field in entry.split()]
        passport = dict()
        for field in fields:
            key, value = field.split(':')
            passport[key] = value
        passports.append(passport)
    return passports


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
    passports = get_passports()
    print(get_number_of_valid_passports(passports))