import re


P_IN = "aoc14-data"
P_IN_S = "aoc14-data-small"


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


def get_sum_of_all_masked_values(mask_groups: list) -> None:
    #   IN: dict of mask and key:values for each
    #   OUT: int, sum of all masked values
    # * create masked values dict
    masked_values = dict()
    # * for each new bitmask in list
    for mask in mask_groups:
        # * for each memory location and value in the bitmask dict
        for loc, value in mask['data'].items():
            # * convert the value to binary string
            bin_value = bin(value)[2:].zfill(36)
            # * for each char in both the mask and the binary string:
            for index in range(36):
                # * if the mask char is a 0, change that binary char to a 0
                if mask['mask'][index] == '0':
                    bin_value = bin_value[:index] + '0' + bin_value[index + 1:]
                # * if the mask char is an 1, change that binary char to a 1
                elif mask['mask'][index] == '1':
                    bin_value = bin_value[:index] + '1' + bin_value[index + 1:]
            # * add that int of string to the memory location of the masked values dict
            masked_values[loc] = int(bin_value, 2)
    # * create sum of 0
    sum = 0
    # * for each key in masked values
    for loc in masked_values:
        # * add value to sum
        sum += masked_values[loc]
    # * return sum
    return sum


if __name__ == "__main__":
    masks = parse_data()
    print(get_sum_of_all_masked_values(masks))