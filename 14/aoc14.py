import re


P_IN = "aoc14-data"
P_IN_S = "aoc14-data-small"
P_IN_S2 = "aoc14-data-small2"


def parse_data():
    # open data file
    with open(P_IN, 'r') as f:
        # make list of contents
        data = f.read().split('\n')
    memory_pattern = re.compile(r'(?<=mem\[)\d+(?=\])')
    value_pattern = re.compile(r'(?<=\s\=\s)\d+$')
    # make list to hold masks and their values [{mask: {mem: value, mem: value}]
    output = []
    bitmask_dict = None
    # for each line in contents
    for line in data:
        # if line starts with "mask = "
        if "mask = " in line:
            # * add to current_head's value dict the key:value pair
            if bitmask_dict is not None: output.append(bitmask_dict)
            # set mask to everything past "mask = "
            mask = line[7:]
            # * create new dict with key as mask and dict as value
            bitmask_dict = {'mask': mask, 'data': dict()}
        else:
            # * set key to number between '[' and ']'
            memory_address = memory_pattern.search(line).group()
            # * set value to number after ' = '
            value = value_pattern.search(line).group()
            bitmask_dict['data'][int(memory_address)] = int(value)
    output.append(bitmask_dict)
    return output


def get_sum_of_all_masked_values(mask_groups: list) -> int:
    masked_values = dict()
    for mask in mask_groups:
        for loc, value in mask['data'].items():
            bin_value = bin(value)[2:].zfill(36)
            for index in range(36):
                if mask['mask'][index] == '0':
                    bin_value = bin_value[:index] + '0' + bin_value[index + 1:]
                elif mask['mask'][index] == '1':
                    bin_value = bin_value[:index] + '1' + bin_value[index + 1:]
            masked_values[loc] = int(bin_value, 2)
    masked_values_sum = 0
    for loc in masked_values:
        masked_values_sum += masked_values[loc]
    return masked_values_sum


def get_sum_of_all_masked_values_part_2(mask_groups: list) -> int:
    masked_values = dict()
    for mask in mask_groups:
        for loc, value in mask['data'].items():
            # make binary location
            bin_loc = bin(loc)[2:].zfill(36)
            # for each char in the loc and the mask
            for index in range(36):
                # if the mask char is a 0, do nothing
                if mask['mask'][index] == '0':
                    pass
                # if the mask char is a 1, change loc at index to 1
                elif mask['mask'][index] == '1':
                    bin_loc = bin_loc[:index] + '1' + bin_loc[index + 1:]
                # else, if 'x'
                else:
                    # change loc at index to 'x'
                    bin_loc = bin_loc[:index] + 'X' + bin_loc[index + 1:]
            memory_locs = get_all_locs(bin_loc)
            for new_loc in memory_locs:
                masked_values[int(new_loc, 2)] = value
    masked_values_sum = 0
    for loc in masked_values:
        masked_values_sum += masked_values[loc]
    return masked_values_sum


def get_all_locs(binary: str) -> list:
    ### edge cases
    ### base case
    # if no X, return the string in an array
    if 'X' not in binary:
        return [binary]
    ### recursive case
    # else, if 1 or more X
    else:
        locs = list()
        # locs += get_all_locs(binary.replace('X', '1', 1))
        locs += get_all_locs(binary.replace('X', '0', 1))
        locs += get_all_locs(binary.replace('X', '1', 1))
        return locs

if __name__ == "__main__":
    masks = parse_data()
    # print(get_sum_of_all_masked_values(masks))
    print(get_sum_of_all_masked_values_part_2(masks))
