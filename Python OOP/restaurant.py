class Restaurant:

    def __init__(self):
        self.menu = {
            "main course": {
                "Burger": 99.00,
                "Fried Chicken": 110.00,
                "Spaghetti": 99.00,
                "Pizza": 80.00,
                "French Fries": 40.00
            },
            "drinks": {
                "Iced Tea": 60.00,
                "Coke": 55.00,
                "Sprite": 55.00,
                "Royal": 55.00
            }
        }

        self.orders = []
        self.subtotal = 0
        self.discount = 0
        self.total = 0

    def display_menu(self):
        print("\n==========================================")
        print("          DELIGHT BITE RESTAURANT")
        print("==========================================")

        for category, items in self.menu.items():
            print(f"\n---------- {category.upper()} -----------")

            for item_name, price in items.items():
                print(f"{item_name:<25} ₱{price:>7.2f}")

        print("==========================================")

    def confirm_ordering(self):
        while True:
            answer = input(
                "\nWould you like to proceed with your order? (yes/no): "
            ).lower().strip()

            if answer == "yes":
                return True

            elif answer == "no":
                return False

            else:
                print("Invalid input. Please enter yes or no.")

    def find_item(self, item_name):
        for category, items in self.menu.items():

            for name, price in items.items():

                if name.lower() == item_name.lower():
                    return name, price

        return None, None

    def take_order(self):
        while True:
            print("-----------------------------------------------")

            item_name = input(
                "Enter the item you want to order: "
            ).strip()

            name, price = self.find_item(item_name)

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

            self.orders.append({
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
                    return

                else:
                    print("Invalid input. Please enter yes or no.")

    def calculate_total(self):
        self.subtotal = 0

        for order in self.orders:
            item_total = order["price"] * order["quantity"]
            self.subtotal += item_total

        while True:
            discount_type = input(
                "\nDiscount type (Senior Citizen/PWD/No): "
            ).lower().strip()

            if discount_type in ["senior", "senior citizen", "pwd"]:
                discount_rate = 0.20
                break

            elif discount_type == "no":
                discount_rate = 0
                break

            else:
                print(
                    "Invalid input. Please enter senior, pwd, or no."
                )

        self.discount = self.subtotal * discount_rate
        self.total = self.subtotal - self.discount

    def print_receipt(self):
        print("\n")
        print("=====================================================")
        print("                DELIGHT BITE RESTAURANT")
        print("                    SALES RECEIPT")
        print("=====================================================")

        print(
            f"{'ITEM':<20}"
            f"{'QTY':>5}"
            f"{'PRICE':>12}"
            f"{'TOTAL':>15}"
        )

        print("-" * 53)

        for order in self.orders:

            item_name = order["item"]
            quantity = order["quantity"]
            price = order["price"]

            item_total = price * quantity

            print(
                f"{item_name:<20}"
                f"{quantity:>4}"
                f"{'₱' + format(price, '.2f'):>14}"
                f"{'₱' + format(item_total, '.2f'):>14}"
            )

        print("-" * 53)

        print(f"{'Subtotal:':<40} ₱{self.subtotal:>10.2f}")
        print(f"{'Discount:':<40} ₱{self.discount:>10.2f}")
        print(f"{'TOTAL:':<40} ₱{self.total:>10.2f}")

        print("=====================================================")
        print("           Thank you for dining with us!")
        print("=====================================================")
