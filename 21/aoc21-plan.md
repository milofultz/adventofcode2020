# Part 1: Problem

Of the ingredients containing no allergens, how many times do those ingredients show up in all of the food in the list?

## Rules:

* Each set of ingredients shows allergens that are definitely present in that set.
* Each allergen is found in exactly one ingredient.
* Allergens aren't always marked.
    * When they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list.
    * Even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.

## Plan:

* IN: list, of 
    * ingredients separated by spaces
    * allergens enclosed by " (contains " and ")"
* OUT: int, number of times ingredients with no allergens appear

### Parse Data

* IN: 
    * list, of 
      * ingredients separated by spaces
      * allergens enclosed by " (contains " and ")"
* OUT: 
    * list of dicts (ingredients: , allergens:)
    * dict of locations by ingredient and by allergen (ingredients: {a: set(),...}, allergens: {a: set(),...)
  
* Load data
* Split data by line
* create output list of dicts
* create locations dict with "ingredients" and "allergen" defaultdicts as a set
* for index in the amount of lines in the data
    * create entry dict
    * split data at index from the right at " (contains "
    * set entry dict "ingredients" to beginning trimmed of whitespace split by spaces
    * for each ingredient in that list
        * in the location: ingredients dict, add the index number to the set at key ingredient
    * set entry dict "allergens" to everything but the last character split by ", "
    * for each allergen in that list
        * in the location: allergen dict, add the index number to the set at key allergen
    * add this entry dict to the output list
* return list and locations

