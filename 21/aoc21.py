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


def find_allergen_free_ingredients(food_list: list, locations: dict) -> list:
    food_list = deepcopy(food_list)
    free_of_allergens = False
    while not free_of_allergens:
        free_of_allergens = True
        allergen_locations = deepcopy(locations["allergens"])
        for allergen, a_locations in allergen_locations.items():
            ing_count = defaultdict(int)
            for loc in a_locations:
                for ing in food_list[loc]["ingredients"]:
                    ing_count[ing] += 1
            if len(a_locations) in ing_count.values():
                free_of_allergens = False
                keys = list(ing_count.keys())
                vals = list(ing_count.values())
                alrg_ing = keys[vals.index(len(a_locations))]
                for loc in locations["ingredients"][alrg_ing]:
                    i = food_list[loc]["ingredients"].index(alrg_ing)
                    del food_list[loc]["ingredients"][i]
                for loc in locations["allergens"][allergen]:
                    i = food_list[loc]["allergens"].index(allergen)
                    del food_list[loc]["allergens"][i]
                del locations["allergens"][allergen]
                del locations["ingredients"][alrg_ing]
        for food in food_list:
            if len(food["ingredients"]) == 1 and len(food["allergens"]) == 1:
                free_of_allergens = False
                alrg_ing = food["ingredients"][0]
                allergen = food["allergens"][0]
                for _ in deepcopy(food_list):
                    food["ingredients"].pop(alrg_ing, None)
                    food["allergens"].pop(allergen, None)
                del locations["allergens"][allergen]
                del locations["ingredients"][alrg_ing]
    return [ing for food in food_list for ing in food["ingredients"]]


if __name__ == "__main__":
    food_list, locations = parse_data(P_IN)
    allergen_free = find_allergen_free_ingredients(food_list, locations)
    print(len(allergen_free))
