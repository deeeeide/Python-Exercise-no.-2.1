def confirm_ordering():
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
