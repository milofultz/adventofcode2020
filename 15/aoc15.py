P_IN = "19,0,5,1,10,13"
P_INS = "1,3,2"
P_EX = "0,3,6"


def get_number_at_turn(final_turn: int, starting_numbers: list) -> int:
    #   IN: list of starting ints
    #       int, turn number to get value of
    #   OUT: int, value considered on provided turn number

    # - define a dict that holds keys (number) and value dict {later_turn: last seen, earlier_turn: -1}
    last_seen = dict()
    turn_counter = 0
    # - for turn and number in starting numbers
    for number in starting_numbers:
        # - create dict key of current number with value as {later_turn: turn, earlier_turn: -1}
        print(f"Starting: {number}")
        last_seen[number] = {"last": turn_counter, "first": -1}
        turn_counter += 1
    # - define previous number as last number in starting numbers list
    previous_number = starting_numbers[-1]
    # - Define the turn counter at length of starting numbers list
    # - while turn counter is less than end turn number
    while turn_counter < final_turn:
        # if previous number is in dict but is the first time seen
        if last_seen[previous_number]["first"] == -1:
            print(f"Seen once: {previous_number}; New number: 0")
            last_seen[0]["first"], last_seen[0]["last"] = (
                last_seen[0]["last"], turn_counter)
            # set previous number to 0
            previous_number = 0
        # - else, if has been seen more than once before
        else:
            # - set current_number to later_turn - last turn
            current_number = last_seen[previous_number]["last"] - last_seen[previous_number]["first"]
            print(f"Seen: {previous_number}; New number: {current_number}")
            # - set dict value of current number to {later_turn: turn_counter, earlier_turn: later_turn}
            if not last_seen.get(current_number):
                last_seen[current_number] = {"last": turn_counter, "first": -1}
            else:
                last_seen[current_number]["first"], last_seen[current_number]["last"] = (
                    last_seen[current_number]["last"], turn_counter)
            # - set previous number to current_number
            previous_number = current_number
        turn_counter += 1
    # - return previous number
    return previous_number


if __name__ == "__main__":
    # - Parse the data.
    starting_numbers = [int(num) for num in P_IN.split(",")]
    # - Get the value of what number will be spoken on the 2020th turn.
    # Make a function that takes in the starting numbers and a turn number as input
    print(get_number_at_turn(2020, starting_numbers))
