IN = "aoc16-data"
INS = "aoc16-data-small"


def parse_input():
    with open(INS, 'r') as f:
        data = f.read()
    split_data = data.rsplit('\n\n')
    fields = parse_fields_data(split_data[0])
    my_ticket = parse_ticket_data(split_data[1])
    nearby_tickets = parse_ticket_data(split_data[2])
    return fields, my_ticket, nearby_tickets


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


if __name__ == "__main__":
    fields, my_ticket, nearby_tickets = parse_input()
    # print(fields, my_ticket, nearby_tickets)
