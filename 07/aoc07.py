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
    bags = bags[:-1].replace(' bags', '').replace(' bag', '').split(', ')
    contents = dict()
    for inner_bag in bags:
        quantity, color = inner_bag.split(' ', 1)
        if quantity.isnumeric():
            contents[color] = int(quantity)
    return contents


def get_bags_containing_color(desired_color: str, lookup: dict) -> set:
    matches = set()
    for entry in lookup.keys():
        if desired_color in get_names_of_bags_contained_in(entry, lookup):
            matches.add(entry)
    return matches


def get_names_of_bags_contained_in(color: str, lookup: dict) -> set:
    contents = set()
    current_bag_contents = lookup.get(color)
    if len(current_bag_contents) is None:
        return contents
    else:
        for bag in current_bag_contents:
            contents.add(bag)
            contents.update(get_names_of_bags_contained_in(bag, lookup))
        return contents


def get_number_of_bags_inside(color: str, lookup: dict) -> int:
    contents = 0
    current_bag_contents = lookup.get(color)
    if len(current_bag_contents) is None:
        return contents
    else:
        for bag, quantity in current_bag_contents.items():
            bags_inside = get_number_of_bags_inside(bag, lookup)
            for i in range(quantity):
                # current bag plus amount of all bags inside
                contents += 1 + bags_inside
        return contents


if __name__ == "__main__":
    bag_contents = get_all_bag_contents()
    print("Bags that eventually contain at least one shiny gold bag: ", end='')
    print(len(get_bags_containing_color('shiny gold', bag_contents)))
    print("Bags that are required to be inside one shiny gold bag: ", end='')
    print(get_number_of_bags_inside('shiny gold', bag_contents))
