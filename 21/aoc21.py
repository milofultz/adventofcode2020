from collections import defaultdict


P_IN = "aoc21-data"
P_INS = "aoc21-data-small"


def parse_data(fp) -> (list, dict):
    # * Load data
    with open(fp, "r") as f:
        # * Split data by line
        data = f.read().split("\n")
    # * create output list of dicts
    food_list = list()
    # * create locations dict with "ingredients" and "allergen" defaultdicts as a set
    locations = {
        "ingredients": defaultdict(set),
        "allergens": defaultdict(set)
    }
    # * for index in the amount of lines in the data
    for i, line in enumerate(data):
        # * create entry dict
        entry = defaultdict(list)
        # * split data at index from the right at " (contains "
        raw_ingredients, raw_allergens = line.rsplit(" (contains ")
        # * set entry dict "ingredients" to beginning trimmed of whitespace split by spaces
        for ingredient in raw_ingredients.strip().split():
            entry["ingredients"].append(ingredient)
            # * in the location: ingredients dict, add the index number to the set at key ingredient
            locations["ingredients"][ingredient].add(i)
        # * set entry dict "allergens" to everything but the last character split by ", "
        for allergen in raw_allergens[:-1].strip().split(", "):
            entry["allergens"].append(allergen)
            # * in the location: ingredients dict, add the index number to the set at key ingredient
            locations["allergens"][allergen].add(i)
        # * add this entry dict to the output list
        food_list.append(entry)
    # * return list and locations
    return food_list, locations



if __name__ == "__main__":
    food_list, locations = parse_data(P_INS)
