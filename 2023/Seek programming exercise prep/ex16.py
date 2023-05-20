def menuorder():
    menu = {
        "burger": 5.00,
        "pizza": 3.00,
        "hotdog": 1.50
    }

    while True:
        order = input("""Please enter your desired order:
              Burger | $5
              Pizza | $3
              Hot Dog | $1.5
              """).lower()

        if order in menu:
            price = menu[order]
            print(f"{order.capitalize()} | ${price:.2f}")
            break
        else:
            print("Invalid Order. Please try again.")

menuorder()