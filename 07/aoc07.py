PUZZLE_INPUT = "aoc07-data"


class Bags:
    def __init__(self, bag_contents):
        self.bag_contents = bag_contents

    def get_bags_containing_color(self, desired_color: str) -> set:
        matches = set()
        for entry in self.bag_contents.keys():
            if desired_color in self.get_names_of_bags_contained_in(entry):
                matches.add(entry)
        return matches

    def get_names_of_bags_contained_in(self, color: str) -> set:
        contents = set()
        current_bag_contents = self.bag_contents.get(color)
        if len(current_bag_contents) is None:
            return contents
        else:
            for bag in current_bag_contents:
                contents.add(bag)
                contents.update(self.get_names_of_bags_contained_in(bag))
            return contents

    def get_number_of_bags_inside(self, color: str) -> int:
        contents = 0
        current_bag_contents = self.bag_contents.get(color)
        if len(current_bag_contents) is None:
            return contents
        else:
            for bag, quantity in current_bag_contents.items():
                bags_inside = self.get_number_of_bags_inside(bag)
                for i in range(quantity):
                    # current bag plus amount of all bags inside
                    contents += 1 + bags_inside
            return contents


def get_all_bag_contents() -> dict:
    with open(PUZZLE_INPUT, 'r') as f:
        bags = f.read().split('\n')
    all_bags = dict()
    for bag in bags:
        outer_bag, inner_bags = bag.split(' bags contain ')
        inner_bags = parse_inner_bags(inner_bags)
        all_bags[outer_bag] = inner_bags
    return all_bags


def parse_inner_bags(inner_bags: str) -> dict:
    inner_bags = inner_bags[:-1].replace(' bags', '').replace(' bag', '').split(', ')
    contents = dict()
    for inner_bag in inner_bags:
        quantity, color = inner_bag.split(' ', 1)
        if quantity.isnumeric():
            contents[color] = int(quantity)
    return contents


if __name__ == "__main__":
    bags = Bags(get_all_bag_contents())
    print("Bags that eventually contain at least one shiny gold bag: ", end='')
    print(len(bags.get_bags_containing_color('shiny gold')))
    print("Bags that are required to be inside one shiny gold bag: ", end='')
    print(bags.get_number_of_bags_inside('shiny gold'))
