IN = "aoc16-data"
INS = "aoc16-data-small"


def parse_input():
    with open(IN, 'r') as f:
        data = f.read()
    split_data = data.rsplit('\n\n')
    fields_data = parse_fields_data(split_data[0])
    my_ticket_data = parse_ticket_data(split_data[1])
    nearby_ticket_data = parse_ticket_data(split_data[2])
    return fields_data, my_ticket_data, nearby_ticket_data


def parse_fields_data(raw_data: str):
    parsed_fields = dict()
    raw_fields = raw_data.split('\n')
    for raw_field in raw_fields:
        field_name, value_ranges = raw_field.split(': ')
        parsed_fields[field_name] = list()
        value_ranges = value_ranges.split(" or ")
        for value_range in value_ranges:
            low_high = tuple(int(value) for value in value_range.split("-"))
            parsed_fields[field_name].append(low_high)
    return parsed_fields


def parse_ticket_data(raw_data: str):
    tickets = raw_data.split(':\n')[1].split('\n')
    parsed_ticket_data = list()
    for ticket in tickets:
        parsed_ticket_data.append([int(num) for num in ticket.split(",")])
    return parsed_ticket_data


def get_invalid_nearby_ticket_numbers(fields: dict, nearby_tickets: list) -> int:
    invalid_sum = 0
    accepted_numbers = get_accepted_numbers(fields)
    for ticket in nearby_tickets:
        for number in ticket:
            invalid_sum += number if number not in accepted_numbers else 0
    return invalid_sum


def get_accepted_numbers(fields: dict):
    numbers = set()
    for _, ranges in fields.items():
        for number_range in ranges:
            lo, hi = number_range
            numbers.update([num for num in range(lo, hi + 1)])
    return numbers


if __name__ == "__main__":
    fields, my_ticket, nearby_tickets = parse_input()
    # print(fields, my_ticket, nearby_tickets)
    print(get_invalid_nearby_ticket_numbers(fields, nearby_tickets))