from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    set_unico = set()
    for element in dish_ingredients:
        if element not in set_unico:
            set_unico.add(element)
    return dish_name, set_unico


def check_drinks(drink_name, drink_ingredients):
    for element in drink_ingredients:
        if element in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"
