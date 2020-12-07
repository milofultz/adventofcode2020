PUZZLE_INPUT = "aoc07-data"


def get_all_bag_contents() -> dict:
    with open(PUZZLE_INPUT, 'r') as f:
        bags = f.read().split('\n')
    all_bags = dict()
    for bag in bags:
        outer_bag, inner_bags = bag.split(' bags contain ')
        inner_bags = parse_inner_bags(inner_bags)
        all_bags[outer_bag] = inner_bags
    return all_bags


def parse_inner_bags(bags: str) -> dict:
    contents = dict()
    bags = bags[:-1].replace(' bags', '').replace(' bag', '').split(', ')
    for inner_bag in bags:
        quantity, color = inner_bag.split(' ', 1)
        if quantity.isnumeric():
            contents[color] = int(quantity)
    return contents


def get_bags_containing_color(desired_color: str, lookup: dict) -> list:
    matches = list()
    for entry in lookup.keys():
        if desired_color in get_total_bag_contents(entry, lookup):
            matches.append(entry)
    return matches


def get_total_bag_contents(color: str, lookup: dict) -> list:
        contents = list()
        current_bag_contents = lookup.get(color)
        if len(current_bag_contents) is None:
            return contents
        else:
            for bag, quantity in current_bag_contents.items():
                for i in range(quantity):
                    contents.append(bag)
                    contents = contents + get_total_bag_contents(bag, lookup)
            return contents


if __name__ == "__main__":
    bag_contents = get_all_bag_contents()
    print(len(get_total_bag_contents('shiny gold', bag_contents)))
