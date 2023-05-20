def positive_negative_checker():
    try:
        reqNumbers = input("Please enter your numbers, separated by commas")
        numberListString = reqNumbers.split(",")
        numberListInt = list(map(int, numberListString))
    except ValueError:
            "Invalid List somehow, please try again"

    for number in numberListInt:
        if number > 0:
            print("Positive, ")
        elif number < 0:
            print("Negative, ")
        else:
            print("Lets have a philosophical debate about whether the number 0 is positive or negative :)")

positive_negative_checker()