# Much simpler/faster refactor inspired by Scarygami:
# https://github.com/Scarygami/aoc2020/blob/main/15/day15.py


P_IN = "19,0,5,1,10,13"
P_INS = "1,3,2"
P_EX = "0,3,6"


def get_number_at_turn(final_turn: int, starting_numbers: list) -> int:
    last_seen = {value: index for index, value in enumerate(starting_numbers)}
    previous_number = starting_numbers[-1]
    for turn in range(len(starting_numbers), final_turn):
        if previous_number not in last_seen:
            current_number = 0
        else:
            current_number = (turn - 1) - last_seen[previous_number]
        last_seen[previous_number] = turn - 1
        previous_number = current_number
        turn += 1
    return previous_number


if __name__ == "__main__":
    starting_numbers = [int(num) for num in P_IN.split(",")]
    print(f"Part 1: {get_number_at_turn(2020, starting_numbers)}")
    print(f"Part 2: {get_number_at_turn(30000000, starting_numbers)}")
