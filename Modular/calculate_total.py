def get_discount_rate():
    while True:
        discount_type = input(
            "\nDiscount type (Senior Citizen/PWD/No): "
        ).lower().strip()

        if discount_type in ["senior", "senior citizen", "pwd"]:
            return 0.20

        elif discount_type == "no":
            return 0

        else:
            print(
                "Invalid input. Please enter senior, pwd, or no."
            )


def calculate_total(orders):
    subtotal = 0

    for order in orders:
        item_total = order["price"] * order["quantity"]
        subtotal += item_total

    discount_rate = get_discount_rate()

    discount = subtotal * discount_rate
    total = subtotal - discount

    return subtotal, discount, total
