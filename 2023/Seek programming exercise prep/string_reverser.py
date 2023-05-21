def string_reverser():
    userInput = input("Please input the string you want to reverse: ")
    userInput = userInput.lower()
    reversedUserInput = ''.join(reversed(userInput))

    print("Original string :", userInput)
    print("Reversed string :", reversedUserInput)

string_reverser()