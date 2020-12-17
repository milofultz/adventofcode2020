import copy


IN = "aoc16-data"
INS = "aoc16-data-small"
INS2 = "aoc16-data-small2"


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
        parsed_fields[field_name] = set()
        value_ranges = value_ranges.split(" or ")
        for value_range in value_ranges:
            low, high = tuple(int(value) for value in value_range.split("-"))
            numbers = [num for num in range(low, high + 1)]
            parsed_fields[field_name].update(numbers)
    return parsed_fields


def parse_ticket_data(raw_data: str):
    tickets = raw_data.split(':\n')[1].split('\n')
    parsed_ticket_data = list()
    for ticket in tickets:
        parsed_ticket_data.append([int(num) for num in ticket.split(",")])
    return parsed_ticket_data


def get_invalid_sum_and_valid_tickets(fields: dict, nearby_tickets: list) -> tuple:
    invalid_sum = 0
    valid_tickets = []
    accepted_numbers = get_accepted_numbers(fields)
    for ticket in nearby_tickets:
        valid = True
        for number in ticket:
            if number not in accepted_numbers:
                invalid_sum += number
                valid = False
        if valid:
            valid_tickets.append(ticket)
    return invalid_sum, valid_tickets


def get_accepted_numbers(fields: dict):
    all_numbers = set()
    for _, numbers in fields.items():
        all_numbers.update(numbers)
    return all_numbers


def get_field_order(fields: dict, valid_tickets: list) -> list:
    # - create a suspected_field list of lists, one for each index of the ticket containing every field name
    all_fields = list(fields.keys())
    suspected_fields = [copy.deepcopy(all_fields) for _ in all_fields]
    # - for each ticket
    for ticket in valid_tickets:
        #- for each index and number in the ticket
        for index, number in enumerate(ticket):
            #- for each field
            for field in all_fields:
                #- if the number is not in the range
                if number not in fields[field] and field in suspected_fields[index]:
                    #- remove it from the suspected sublist for that index
                    suspected_fields[index].remove(field)
    # remove assured fields from other indexes
    return simplify_fields(suspected_fields)


def simplify_fields(fields: list) -> list:
    fields = copy.deepcopy(fields)
    found_fields = set()
    simplified = False
    while not simplified:
        simplified = True
        for field in fields:
            if len(field) == 1:
                found_fields.add(field[0])
            else:
                simplified = False
                for subfield in field:
                    if subfield in found_fields:
                        field.remove(subfield)
    return sum(fields, [])



if __name__ == "__main__":
    fields, my_ticket, nearby_tickets = parse_input()
    invalid_sum, valid_tickets = get_invalid_sum_and_valid_tickets(fields, nearby_tickets)
    print(invalid_sum)
    field_order = get_field_order(fields, valid_tickets)
    departure_mult = 1
    for field, number in zip(field_order, my_ticket[0]):
        print(field, number)
        if "departure" in field:
            departure_mult = number * departure_mult
    print(departure_mult)
    # print(field_order)
    # print(my_ticket)
