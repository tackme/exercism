from collections import Counter

def create_inventory(items: list) -> dict:
    '''

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    '''

    inventory = Counter(items)

    return dict(inventory)

def add_items(inventory: dict, items: list) -> dict:
    '''

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    '''

    for item in items:
        inventory[item] = inventory.get(item, 0)
        inventory[item] += 1

    return inventory


def delete_items(inventory: dict, items: list) -> dict:
    '''

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to remove from the inventory.
    :return:  dict - updated inventory dictionary with items removed.
    '''

    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def list_inventory(inventory: dict) -> list:
    '''

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    '''

    return [item for item in inventory.items() if item[1] != 0]
