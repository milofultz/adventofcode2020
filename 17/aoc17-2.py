import copy
import numpy as np


P_IN = 'aoc17-data'
P_INS = 'aoc17-data-small'
ACTIVE = '#'
INACTIVE = '.'


def make_array_from_input(fp: str):
    """ Return 4D array from input """
    with open(fp, 'r') as f:
        raw_array = f.read().split('\n')
    return np.array([[[[letter for letter in line] for line in raw_array]]])


def play_game(init_dimension: np.array, turns: int) -> np.array:
    """ Return resulting array after X turns """
    result_dimension = copy.deepcopy(init_dimension)
    for turn in range(turns):
        result_dimension = expand_array_to_fit(result_dimension)
        working_dimension = copy.deepcopy(result_dimension)
        for index, element in np.ndenumerate(result_dimension):
            active_neighbors = get_active_neighbors(index, result_dimension)
            if element == ACTIVE and active_neighbors not in [2, 3]:
                working_dimension[index] = INACTIVE
            elif element == INACTIVE and active_neighbors == 3:
                working_dimension[index] = ACTIVE
        result_dimension = working_dimension
    return result_dimension


def get_active_neighbors(index: tuple, array: np.array) -> int:
    # Create subarray to search within
    z_low, z_high, y_low, y_high, x_low, x_high, w_low, w_high = (
        get_search_ranges_from_index(index, array))
    search_array = array[z_low:z_high, y_low:y_high, x_low:x_high, w_low:w_high]

    # Return total, and don't count self
    total = np.count_nonzero(search_array == ACTIVE)
    return total if array[index] != ACTIVE else total - 1


def get_search_ranges_from_index(index, array):
    z_index, y_index, x_index, w_index = index
    z_max, y_max, x_max, w_max = (np.size(array, 0), np.size(array, 1),
                                  np.size(array, 2), np.size(array, 3))

    # Set z, y, x search boundaries based on edges
    if z_index == 0: z_low, z_high = z_index, z_index+2
    elif z_index == z_max: z_low, z_high = z_index-1, z_index+1
    else: z_low, z_high = z_index-1, z_index+2

    if y_index == 0: y_low, y_high = y_index, y_index+2
    elif y_index == y_max: y_low, y_high = y_index-1, y_index+1
    else: y_low, y_high = y_index-1, y_index+2

    if x_index == 0: x_low, x_high = x_index, x_index+2
    elif x_index == x_max: x_low, x_high = x_index-1, x_index+1
    else: x_low, x_high = x_index-1, x_index+2

    if w_index == 0: w_low, w_high = w_index, w_index+2
    elif w_index == w_max: w_low, w_high = w_index-1, w_index+1
    else: w_low, w_high = w_index-1, w_index+2

    return z_low, z_high, y_low, y_high, x_low, x_high, w_low, w_high


def expand_array_to_fit(array: np.array) -> np.array:
    expanded = copy.deepcopy(array)
    z_max, y_max, x_max, w_max = (np.size(expanded, 0), np.size(expanded, 1),
                                  np.size(expanded, 2), np.size(expanded, 3))

    # if there are any active cubes on outer side of axis, concatenate a
    # fully inactive flat array to that side and add to total size of axis
    if np.count_nonzero(expanded[0, 0:, 0:] == ACTIVE) != 0:
        expanded = np.concatenate((np.full((1, y_max, x_max, w_max), '.'),
                                   expanded), 0)
        z_max += 1
    if np.count_nonzero(expanded[z_max-1, 0:, 0:] == ACTIVE) != 0:
        expanded = np.concatenate((expanded,
                                   np.full((1, y_max, x_max, w_max), '.')), 0)
        z_max += 1
    if np.count_nonzero(expanded[0:, 0, 0:] == ACTIVE) != 0:
        expanded = np.concatenate((np.full((z_max, 1, x_max, w_max), '.'),
                                   expanded), 1)
        y_max += 1
    if np.count_nonzero(expanded[0:, y_max-1, 0:] == ACTIVE) != 0:
        expanded = np.concatenate((expanded,
                                   np.full((z_max, 1, x_max, w_max), '.')), 1)
        y_max += 1
    if np.count_nonzero(expanded[0:, 0:, 0] == ACTIVE) != 0:
        expanded = np.concatenate((np.full((z_max, y_max, 1, w_max), '.'),
                                   expanded), 2)
        x_max += 1
    if np.count_nonzero(expanded[0:, 0:, x_max-1] == ACTIVE) != 0:
        expanded = np.concatenate((expanded,
                                   np.full((z_max, y_max, 1, w_max), '.')), 2)
        x_max += 1
    if np.count_nonzero(expanded[0:, 0:, 0:, 0] == ACTIVE) != 0:
        expanded = np.concatenate((np.full((z_max, y_max, x_max, 1), '.'),
                                   expanded), 3)
        w_max += 1
    if np.count_nonzero(expanded[0:, 0:, 0:, w_max-1] == ACTIVE) != 0:
        expanded = np.concatenate((expanded,
                                   np.full((z_max, y_max, x_max, 1), '.')), 3)
        w_max += 1
    return expanded


if __name__ == "__main__":
    initial_config = make_array_from_input(P_IN)
    result = play_game(initial_config, 6)
    print(np.count_nonzero(result == ACTIVE))
