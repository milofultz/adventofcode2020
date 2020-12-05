def byr(data):
    if 1920 <= int(data) <= 2002:
        return True
    return False


def iyr(data):
    if 2010 <= int(data) <= 2020:
        return True
    return False


def eyr(data):
    if 2020 <= int(data) <= 2030:
        return True
    return False


def hgt(data):
    num, measure = int(data[:-2]), data[-2:]
    if 'cm' in measure and 150 <= num <= 193 or 'in' in measure and 59 <= num <= 76:
        return True
    return False


def hcl(data):
    if len(data) == 7 and data[0] == '#' and data[1:].isalnum():
        return True
    return False


def ecl(data):
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if data in valid:
        return True
    return False


def pid(data):
    if len(data) == 9 and data.isnumeric():
        return True
    return False


validation_dict = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid
}
