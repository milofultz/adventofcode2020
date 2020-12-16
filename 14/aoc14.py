import re


P_IN = "aoc14-data"
P_IN_S = "aoc14-data-small"


def parse_data():
    # open data file
    with open(P_IN_S, 'r') as f:
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
            bitmask_dict = {mask: dict()}
        else:
            # * set key to number between '[' and ']'
            memory_address = memory_pattern.search(line).group()
            # * set value to number after ' = '
            value = value_pattern.search(line).group()
            bitmask_dict[mask] = {memory_address: value}
    output.append(bitmask_dict)
    return output


def part1(masks: list) -> None:
    pass


if __name__ == "__main__":
    bitmasks_with_mem_and_values = parse_data()
    print(bitmasks_with_mem_and_values)
    # get sum of all masked values
    #   IN: dict of mask and key:values for each
    #   OUT: int, sum of all masked values
    #     * create masked values dict
    #     * for each new bitmask in list
    #         * for each memory location and value in the bitmask dict
    #             * convert the value to binary string
    #             * for each char in both the mask and the binary string:
    #                 * if the mask char is a 0, change that binary char to a 0
    #                 * if the mask char is an 1, change that binary char to a 1
    #                 * else, continue
    #             * get int of that string
    #             * add that int to the memory location of the masked values dict
    #     * create sum of 0
    #     * for each key in masked values
    #         * add value to sum
    #     * return sum