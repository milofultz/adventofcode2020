import numpy as np


P_IN = "aoc20-data"
P_INS = "aoc20-data-small"


def parse_data(fp: str) -> dict:
    with open(fp, 'r') as f:
        data = f.read().split("\n\n")
    output = dict()
    for entry in data:
        key, value = entry.split("\n", 1)
        key = key[5:-1]
        value = parse_array(value)
        output[key] = value
    return output


def parse_array(raw: str) -> np.array:
    array = []
    for line in raw.split("\n"):
        array.append(list(line))
    return np.array(array)


if __name__ == "__main__":
    tileset = parse_data(P_INS)
