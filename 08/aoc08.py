import copy


PUZZLE_INPUT = 'aoc08-data'


def get_instructions() -> list:
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read().split('\n')
    output = list()
    for line in data:
        instruction = dict()
        inst_type, val = line.split(' ')
        val = int(val)
        instruction['type'] = inst_type
        instruction['val'] = val
        output.append(instruction)
    return output


def get_accumulator_on_infinite_loop(instructions: list) -> int:
    result = get_accumulator_and_completion_type(instructions)
    return result['accumulator'] if result['end_type'] == 'loop' else None


def get_accumulator_with_fixed_instruction(instructions) -> int:
    for index, instruction in enumerate(instructions):
        if instruction['type'] in ['nop', 'jmp']:
            new_instructions = copy.deepcopy(instructions)
            changed_instruction = copy.deepcopy(instruction)
            changed_instruction['type'] = 'jmp' if instruction['type'] == 'nop' else 'nop'
            new_instructions[index] = changed_instruction
            result = get_accumulator_and_completion_type(new_instructions)
            if result['end_type'] == 'complete':
                return result['accumulator']
    return None


def get_accumulator_and_completion_type(instructions: list) -> dict:
    instructions_length = len(instructions)
    indexes_visited = set()
    accumulator = 0
    current_index = 0
    while current_index not in indexes_visited:
        indexes_visited.add(current_index)
        current_instruction = instructions[current_index]
        if current_instruction['type'] == 'acc':
            accumulator += current_instruction['val']
            current_index += 1
        elif current_instruction['type'] == 'jmp':
            current_index += current_instruction['val']
        elif current_instruction['type'] == 'nop':
            current_index += 1
        if current_index == instructions_length:
            return {'accumulator': accumulator, 'end_type': 'complete'}
    return {'accumulator': accumulator, 'end_type': 'loop'}


if __name__ == "__main__":
    instructions = get_instructions()
    print(get_accumulator_on_infinite_loop(instructions))
    print(get_accumulator_with_fixed_instruction(instructions))
