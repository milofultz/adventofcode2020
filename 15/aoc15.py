P_IN = "19,0,5,1,10,13"
P_INS = "1,3,2"
P_EX = "0,3,6"


def get_number_at_turn(final_turn: int, starting_numbers: list) -> int:
    last_seen = dict()
    turn_counter = 0
    for number in starting_numbers:
        print(f"Starting: {number}")
        last_seen[number] = {"last": turn_counter, "first": -1}
        turn_counter += 1
    previous_number = starting_numbers[-1]
    while turn_counter < final_turn:
        if last_seen[previous_number]["first"] == -1:
            print(f"Seen once: {previous_number}; New number: 0")
            last_seen[0]["first"], last_seen[0]["last"] = (
                last_seen[0]["last"], turn_counter)
            previous_number = 0
        else:
            current_number = last_seen[previous_number]["last"] - last_seen[previous_number]["first"]
            print(f"Seen: {previous_number}; New number: {current_number}")
            if not last_seen.get(current_number):
                last_seen[current_number] = {"last": turn_counter, "first": -1}
            else:
                last_seen[current_number]["first"], last_seen[current_number]["last"] = (
                    last_seen[current_number]["last"], turn_counter)
            previous_number = current_number
        turn_counter += 1
    return previous_number


if __name__ == "__main__":
    starting_numbers = [int(num) for num in P_IN.split(",")]
    print(get_number_at_turn(2020, starting_numbers))
