from find_item import find_item


def take_order():
    orders = []

    while True:
        print("-----------------------------------------------")

        item_name = input(
            "Enter the item you want to order: "
        ).strip()

        name, price = find_item(item_name)

        if name is None:
            print("Sorry, that item is not on the menu.")
            continue

        while True:
            try:
                quantity = int(
                    input(f"Enter quantity for {name}: ")
                )

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                else:
                    break

            except ValueError:
                print(
                    "Invalid quantity. Please enter a whole number."
                )

        orders.append({
            "item": name,
            "quantity": quantity,
            "price": price
        })

        while True:
            another = input(
                "Would you like to order another item? (yes/no): "
            ).lower().strip()

            if another == "yes":
                break

            elif another == "no":
                return orders

            else:
                print("Invalid input. Please enter yes or no.")
