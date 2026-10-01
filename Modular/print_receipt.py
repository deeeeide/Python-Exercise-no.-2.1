def print_receipt(orders, subtotal, discount, total):

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

    for order in orders:
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
    print(f"{'Subtotal:':<40} ₱{subtotal:>10.2f}")
    print(f"{'Discount:':<40} ₱{discount:>10.2f}")
    print(f"{'TOTAL:':<40} ₱{total:>10.2f}")

    print("=====================================================")
    print("           Thank you for dining with us!")
    print("=====================================================")
