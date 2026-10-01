from restaurant import Restaurant


def main():
    restaurant = Restaurant()

    restaurant.display_menu()

    if not restaurant.confirm_ordering():
        print("\nThank you for visiting Delight Bite Restaurant!")
        return

    restaurant.take_order()
    restaurant.calculate_total()
    restaurant.print_receipt()


main()
