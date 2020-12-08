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


def get_accumulator_on_infinite_loop(instructions: list) -> int:
    visited_instructions = set()
    accumulator = 0
    instruction_index = 0
    while instruction_index not in visited_instructions:
        visited_instructions.add(instruction_index)
        current_instruction = instructions[instruction_index]
        print(current_instruction['type'])
        if current_instruction['type'] == 'acc':
            accumulator += current_instruction['val']
            instruction_index += 1
        elif current_instruction['type'] == 'jmp':
            instruction_index += current_instruction['val']
        elif current_instruction['type'] == 'nop':
            instruction_index += 1
        else:
            print('ELSE ERROR in loop')
            instruction_index += 1
    return accumulator


if __name__ == "__main__":
    instructions = get_instructions()
    print(get_accumulator_on_infinite_loop(instructions))