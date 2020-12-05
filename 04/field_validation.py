def byr(data):
    return True if 1920 <= int(data.strip()) <= 2002 else False


def iyr(data):
    return True if 2010 <= int(data.strip()) <= 2020 else False


def eyr(data):
    return True if 2020 <= int(data.strip()) <= 2030 else False


def hgt(data):
    data = data.strip()
    if 'cm' in data[-2:] and 150 <= int(data[:-2]) <= 193:
        return True
    if 'in' in data[-2:] and 59 <= int(data[:-2]) <= 76:
        return True
    return False


def hcl(data):
    data = data.strip()
    return True if len(data) == 7 and data[0] == '#' and data[1:].isalnum() else False


def ecl(data):
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return True if data.strip() in valid else False


def pid(data):
    data = data.strip()
    return True if len(data) == 9 and data.isnumeric() else False


validation_dict = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid
}