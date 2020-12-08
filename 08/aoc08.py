import copy


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


def find_corrupted_instruction(instructions) -> int:
    number_of_instructions = len(instructions)
    def get_accumulator_if_uncorrupted_instruction(new_instructions):
        visited_instructions = set()
        accumulator = 0
        instruction_index = 0
        while instruction_index not in visited_instructions:
            visited_instructions.add(instruction_index)
            current_instruction = new_instructions[instruction_index]
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
            if instruction_index == number_of_instructions:
                return accumulator
        return None
    for index, instruction in enumerate(instructions):
        instructions_copy = copy.deepcopy(instructions)
        instruction_copy = copy.deepcopy(instruction)
        if instruction['type'] in ['nop', 'jmp']:
            instruction_copy['type'] = 'jmp' if instruction['type'] == 'nop' else 'nop'
            instructions_copy[index] = instruction_copy
            val = get_accumulator_if_uncorrupted_instruction(instructions_copy)
            if val is not None:
                return val
    return None




if __name__ == "__main__":
    instructions = get_instructions()
    print(get_accumulator_on_infinite_loop(instructions))
    print(find_corrupted_instruction(instructions))