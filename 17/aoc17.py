import numpy as np


P_IN = 'aoc17-data'
ACTIVE = '#'
INACTIVE = '.'


def make_array_from_input():
    # Open file
    with open(P_IN, 'r') as f:
        # Put data split by newline into variable
        raw_array = f.read().split('\n')
    # Make array containing an array containing another array for each line in the data
    return np.array([[[letter for letter in line] for line in raw_array]])


if __name__ == "__main__":
    initial_config = make_array_from_input()
    print(initial_config)