from menu import menu


def find_item(item_name):
    for category, items in menu.items():
        for name, price in items.items():

            if name.lower() == item_name.lower():
                return name, price

    return None, None
