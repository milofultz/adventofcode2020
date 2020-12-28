from collections import defaultdict


P_IN = "aoc21-data"
P_INS = "aoc21-data-small"


def parse_data(fp) -> (list, dict):
    with open(fp, "r") as f:
        data = f.read().split("\n")
    food_list = list()
    locations = {"ingredients": defaultdict(set),
                 "allergens": defaultdict(set)}
    for i, line in enumerate(data):
        entry = defaultdict(list)
        raw_ingredients, raw_allergens = line.rsplit(" (contains ")
        for ingredient in raw_ingredients.strip().split():
            entry["ingredients"].append(ingredient)
            locations["ingredients"][ingredient].add(i)
        for allergen in raw_allergens[:-1].strip().split(", "):
            entry["allergens"].append(allergen)
            locations["allergens"][allergen].add(i)
        food_list.append(entry)
    return food_list, locations


if __name__ == "__main__":
    food_list, locations = parse_data(P_INS)
