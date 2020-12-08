# part 1
#
# - Input: instruction type, value
# - Output: accumulator value
# - Constraints: None
# - Edge: None
#
#
# Type:
# list of dicts; dict holds inst, val int, visited bool


PUZZLE_INPUT = 'aoc08-data'


def get_instructions():
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read().split('\n')
    instructions = list()
    for line in data:
        instruction = dict()
        inst_type, val = line.split(' ')
        val = int(val)
        instruction['type'] = inst_type
        instruction['val'] = val
        instructions.append(instruction)
    return instructions


if __name__ == "__main__":
    # parse data into list of dicts
    instructions = get_instructions()
    # get accumulator when already visited starting at inst 0
