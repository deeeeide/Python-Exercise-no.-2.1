from menu import menu


def display_menu():
    print("\n==========================================")
    print("          DELIGHT BITE RESTAURANT")
    print("==========================================")

    for category, items in menu.items():
        print(f"\n---------- {category.upper()} -----------")

        for item_name, price in items.items():
            print(f"{item_name:<25} ₱{price:>7.2f}")

    print("==========================================")
