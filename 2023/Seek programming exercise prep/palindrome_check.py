def palindrome_check():
    userInput = input("Input your desired word: ")

    userInput = userInput.replace(" ", "".lower())
    #join lets you convert from memory address to string
    reversedUserInput = ''.join(reversed(userInput))

    print(f"Word is {userInput}")
    print(f"Reversed word is {reversedUserInput}")
    if userInput == reversedUserInput:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

palindrome_check()