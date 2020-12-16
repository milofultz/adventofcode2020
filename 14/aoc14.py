import re


P_IN = "aoc14-data"
P_IN_S = "aoc14-data-small"
P_IN_S2 = "aoc14-data-small2"


def parse_data():
    with open(P_IN, 'r') as f:
        data = f.read().split('\n')
    loc_pattern = re.compile(r'(?<=mem\[)\d+(?=])')
    value_pattern = re.compile(r'(?<=\s=\s)\d+$')
    output = []
    mask_dict = None
    for line in data:
        if "mask = " in line:
            if mask_dict is not None:
                output.append(mask_dict)
            mask = line[7:]
            mask_dict = {'mask': mask, 'data': dict()}
        else:
            loc = loc_pattern.search(line).group()
            value = value_pattern.search(line).group()
            mask_dict['data'][int(loc)] = int(value)
    output.append(mask_dict)
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
            bin_loc = bin(loc)[2:].zfill(36)
            for index in range(36):
                if mask['mask'][index] == '1':
                    bin_loc = bin_loc[:index] + '1' + bin_loc[index + 1:]
                elif mask['mask'][index] == 'X':
                    bin_loc = bin_loc[:index] + 'X' + bin_loc[index + 1:]
            wildcard_locs = get_wildcard_locs(bin_loc)
            for new_loc in wildcard_locs:
                masked_values[int(new_loc, 2)] = value
    masked_values_sum = 0
    for loc in masked_values:
        masked_values_sum += masked_values[loc]
    return masked_values_sum


def get_wildcard_locs(binary: str) -> list:
    if 'X' not in binary:
        return [binary]
    else:
        locs = get_wildcard_locs(binary.replace('X', '0', 1))
        locs += get_wildcard_locs(binary.replace('X', '1', 1))
        return locs


if __name__ == "__main__":
    masks = parse_data()
    print(get_sum_of_all_masked_values(masks))
    print(get_sum_of_all_masked_values_part_2(masks))
