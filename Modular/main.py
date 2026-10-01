from display_menu import display_menu
from confirm_ordering import confirm_ordering
from take_order import take_order
from calculate_total import calculate_total
from print_receipt import print_receipt


def main():

    display_menu()

    if not confirm_ordering():
        print("\nThank you for visiting Delight Bite Restaurant!")
        return

    orders = take_order()

    subtotal, discount, total = calculate_total(orders)

    print_receipt(orders, subtotal, discount, total)


main()
