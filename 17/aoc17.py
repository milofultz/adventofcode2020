import copy
import numpy as np


P_IN = 'aoc17-data'
P_INS = 'aoc17-data-small'
ACTIVE = '#'
INACTIVE = '.'


def make_array_from_input(fp: str):
    # Open file
    with open(fp, 'r') as f:
        # Put data split by newline into variable
        raw_array = f.read().split('\n')
    # Make array containing an array containing another array for each line in the data
    return np.array([[[letter for letter in line] for line in raw_array]])


def play_game(init_dimension: np.array, turns: int) -> np.array:
    # - create deepcopy of input array as 'result'
    result_dimension = copy.deepcopy(init_dimension)
    # - for each turn in X turns
    for turn in range(turns):
        # - create deepcopy of result array as 'working'
        result_dimension = expand_array_to_fit(result_dimension)
        working_dimension = copy.deepcopy(result_dimension)
        # - for each index and element in 3d array
        for index, element in np.ndenumerate(result_dimension):
            # - get number of active neighbors(index, result)
            active_neighbors = get_active_neighbors(index, result_dimension)
            # - if element is active AND active neighbors is less than 2 OR active neighbors is greater than 3
            if element == ACTIVE and active_neighbors not in [2, 3]:
                print(f"{element} to Inactive at {index}")
                # - Set element to inactive in 'working' at index
                working_dimension[index] = INACTIVE
            # - elif element is inactive AND active neighbors is 3
            elif element == INACTIVE and active_neighbors == 3:
                print(f"{element} to Active at {index}")
                # - set element to active in 'working' at index
                working_dimension[index] = ACTIVE
        # - expand array to fit next turn's active()
        # - set 'working' array to result
        result_dimension = working_dimension
    return result_dimension


def get_active_neighbors(index: tuple, array: np.array) -> int:
    # - set z_max to length of z axis
    # - set y_max to length of y axis
    # - set x_max to length of x axis
    z_max, y_max, x_max = np.size(array, 0), np.size(array, 1), np.size(array, 2)
    z_index, y_index, x_index = index

    # - if z index is 0, set z_range to "z_index:z_index+2"
    if z_index == 0: z_low, z_high = z_index, z_index+2
    # - elif z index is z_max, set z_range to "z_index-1:z_index+1"
    elif z_index == z_max: z_low, z_high = z_index-1, z_index+1
    # - else "z_index-1:z_index+2"
    else: z_low, z_high = z_index-1, z_index+2
    
    # - if y index is 0, set y_range to "y_index:y_index+2"
    if y_index == 0: y_low, y_high = y_index, y_index+2
    # - elif y index is y_max, set y_range to "y_index-1:y_index+1"
    elif y_index == y_max: y_low, y_high = y_index-1, y_index+1
    # - else "y_index-1:y_index+2"
    else: y_low, y_high = y_index-1, y_index+2

    # - if x index is 0, set x_range to "x_index:x_index+2"
    if x_index == 0: x_low, x_high = x_index, x_index+2
    # - elif x index is x_max, set x_range to "x_index-1:x_index+1"
    elif x_index == x_max: x_low, x_high = x_index-1, x_index+1
    # - else, set x_range to "x_index-1:x_index+2"
    else: x_low, x_high = x_index-1, x_index+2

    # - make search array from input array (search_area = input[x_range, y_range, z_range])
    search_array = array[z_low:z_high, y_low:y_high, x_low:x_high]
    # - return number of active in search area (np.count_nonzero(condition))
    # don't count self in count
    total = np.count_nonzero(search_array == ACTIVE)
    return total if array[index] != ACTIVE else total - 1



def expand_array_to_fit(array: np.array) -> np.array:
    # - Make deepcopy of input array 'working'
    expanded = copy.deepcopy(array)
    # - for z, get max
    # - for y, get max
    # - for x, get max
    z_max, y_max, x_max = np.size(array, 0), np.size(array, 1), np.size(array, 2)

    # - if there are any active cubes on face (0) of z axis
    if np.count_nonzero(expanded[0, 0:, 0:] == ACTIVE) != 0:
        # - add a layer full of inactive to face of z axis on 'working'
        expanded = np.concatenate((np.full((1, y_max, x_max), '.'),
                                   expanded), 0)
        z_max += 1
    # - if there are any active cubes on back (max) of z axis
    if np.count_nonzero(expanded[z_max-1, 0:, 0:] == ACTIVE) != 0:
        # - add a layer full of inactive to back of z axis on 'working'
        expanded = np.concatenate((expanded,
                                   np.full((1, y_max, x_max), '.')), 0)
        z_max += 1
    # - if there are any active cubes on face (0) of y axis
    if np.count_nonzero(expanded[0:, 0, 0:] == ACTIVE) != 0:
        # - add a layer full of inactive to face of y axis on 'working'
        expanded = np.concatenate((np.full((z_max, 1, x_max), '.'),
                                   expanded), 1)
        y_max += 1
    # - if there are any active cubes on back (max) of y axis
    if np.count_nonzero(expanded[0:, y_max-1, 0:] == ACTIVE) != 0:
        # - add a layer full of inactive to back of y axis on 'working'
        expanded = np.concatenate((expanded,
                                   np.full((z_max, 1, x_max), '.')), 1)
        y_max += 1
    # - if there are any active cubes on face (0) of x axis
    if np.count_nonzero(expanded[0:, 0:, 0] == ACTIVE) != 0:
        # - add a layer full of inactive to face of x axis on 'working'
        expanded = np.concatenate((np.full((z_max, y_max, 1), '.'),
                                   expanded), 2)
        x_max += 1
    # - if there are any active cubes on back (max) of x axis
    if np.count_nonzero(expanded[0:, 0:, x_max-1] == ACTIVE) != 0:
        # - add a layer full of inactive to back of x axis on 'working'
        expanded = np.concatenate((expanded,
                                   np.full((z_max, y_max, 1), '.')),
                                  2)
        x_max += 1
    return expanded


if __name__ == "__main__":
    # initial_config = make_array_from_input(P_IN)
    # result = play_game(initial_config, 6)
    initial_config = make_array_from_input(P_INS)
    result = play_game(initial_config, 1)
    print(np.count_nonzero(result == ACTIVE))
    # print(get_active_neighbors((0,7,6), initial_config))
    # print(expand_array_to_fit(initial_config))
