from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name: str, dish_ingredients: list) -> tuple:
    '''

    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    '''

    return (dish_name, set(dish_ingredients))



def check_drinks(drink_name: str, drink_ingredients: list) -> str:
    '''

    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    '''

    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return f"{drink_name} Mocktail"

    return f"{drink_name} Cocktail"

def categorize_dish(dish_name: str, dish_ingredients: list) -> str:
    '''

    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `categories.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    '''

    if set(dish_ingredients).issubset(VEGAN):
        return f"{dish_name}: VEGAN"

    if set(dish_ingredients).issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"

    if set(dish_ingredients).issubset(PALEO):
        return f"{dish_name}: PALEO"

    if set(dish_ingredients).issubset(KETO):
        return f"{dish_name}: KETO"

    return f"{dish_name}: OMNIVORE"

def tag_special_ingredients(dish: tuple) -> tuple:
    '''

    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `categories.py`.
    '''

    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)



def compile_ingredients(dishes: list) -> set:
    '''

    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    '''

    return set.union(*dishes)



def separate_appetizers(dishes, appetizers):
    '''

    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    '''

    return set(dishes) - set(appetizers)



def singleton_ingredients(dishes: list, intersection: set) -> set:
    '''

    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    '''

    singletons = (dish - intersection for dish in dishes)

    return set.union(*singletons)
