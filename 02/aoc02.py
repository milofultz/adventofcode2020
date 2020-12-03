import re


PASSWORDS = "aoc02-data"


# Get data
def load_data(fp):
    with open(fp, 'r') as f:
        data = f.read()
    return data


def check_entries(entries):
    output = 0
    for entry in entries:
        raw_pattern, password = entry.split(': ')
        amount, char = raw_pattern.split(' ')
        pattern = re.compile(char + "{" + amount + "}")
        output += 1 if pattern.search(password) else 0
    return output
  

def is_password_valid(pattern, string):
    pass


# Print all results on page
#   If failed, ❌ in red with why
#   If correct, ✅ in green with why


if __name__ == "__main__":
    queries = load_data(PASSWORDS).split('\n')
    print(queries)
