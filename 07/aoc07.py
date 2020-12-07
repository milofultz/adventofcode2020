PUZZLE_INPUT = "aoc07-data"


def get_all_bag_contents() -> dict:
    # load data
    with open(PUZZLE_INPUT, 'r') as f:
        bags = f.read().split('\n')
    # create dict to hold color: contents
    all_bags = dict()
    # for each line in data
    for bag in bags:
        # split at 'bags contain'; result is outer bag and inner bags
        outer_bag, inner_bags = bag.split(' bags contain ')
        # remove period from end of inner bags
        inner_bags = inner_bags[:-1]
        # split inner bags at commas
        # bag contents is a dict of color: quantity
        bag_contents = parse_inner_bags(inner_bags)
        # add each to bag contains dict
        all_bags[outer_bag] = bag_contents
    return all_bags


def parse_inner_bags(bags: str) -> dict:
    contents = dict()
    bags = bags.replace(' bags', '').replace(' bag', '').split(', ')
    for inner_bag in bags:
        quantity, color = inner_bag.split(' ', 1)
        if quantity.isnumeric():
            contents[color] = int(quantity)
    return contents


def get_bags_containing_color(desired_color: str, lookup: dict) -> set:
    def get_bag_contents(color: str) -> set:
        contents = set()
        current_bag_contents = lookup.get(color).keys()
        if len(current_bag_contents) is None:
            return contents
        else:
            contents.update(current_bag_contents)
            for bag in current_bag_contents:
                contents.update(get_bag_contents(bag))
            return contents
    matches = set()
    for entry in lookup.keys():
        if desired_color in get_bag_contents(entry):
            matches.add(entry)
    return matches


if __name__ == "__main__":
    # create a lookup table of each bags contents
    bag_contents = get_all_bag_contents()
    # see if bags contents hold a gold bag
    print(len(get_bags_containing_color('shiny gold', bag_contents)))