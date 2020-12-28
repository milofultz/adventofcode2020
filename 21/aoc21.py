from collections import defaultdict
from copy import deepcopy


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


def categorize_ingredients(food_list: list, locations: dict) -> (list, list):
    food_list = deepcopy(food_list)
    free_of_allergens = False
    dangerous = dict()
    while not free_of_allergens:
        free_of_allergens = True
        allergen_locations = deepcopy(locations["allergens"])
        for allergen, allergen_locations in allergen_locations.items():
            ingredient_count = defaultdict(int)
            for index in allergen_locations:
                for ingredient in food_list[index]["ingredients"]:
                    ingredient_count[ingredient] += 1
            if len(allergen_locations) in ingredient_count.values():
                free_of_allergens = False
                names = list(ingredient_count.keys())
                counts = list(ingredient_count.values())
                found_ingredient = names[counts.index(len(allergen_locations))]
                dangerous[allergen] = found_ingredient
                for index in locations["ingredients"][found_ingredient]:
                    x = food_list[index]["ingredients"].index(found_ingredient)
                    del food_list[index]["ingredients"][x]
                for index in locations["allergens"][allergen]:
                    x = food_list[index]["allergens"].index(allergen)
                    del food_list[index]["allergens"][x]
                del locations["allergens"][allergen]
                del locations["ingredients"][found_ingredient]
        for food in food_list:
            if len(food["ingredients"]) == 1 and len(food["allergens"]) == 1:
                free_of_allergens = False
                found_ingredient = food["ingredients"][0]
                allergen = food["allergens"][0]
                food["ingredients"].pop(found_ingredient, None)
                food["allergens"].pop(allergen, None)
                del locations["allergens"][allergen]
                del locations["ingredients"][found_ingredient]
    no_allergens = [ing for food in food_list for ing in food["ingredients"]]
    return no_allergens, dangerous


if __name__ == "__main__":
    food_list, locations = parse_data(P_IN)
    allergen_free, dangerous = categorize_ingredients(food_list, locations)
    print(len(allergen_free))
    print(",".join(x[1] for x in sorted(dangerous.items(), key=lambda x: x[0])))
