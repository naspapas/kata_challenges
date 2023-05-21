def sum_of_digits():
    digits = (input("Please input your desired digits, eg \"12345\" will be handled as 1 + 2 + 3 + 4 + 5 : " ))
    x = 0

    while x < len(digits) - 1:
        y = int(digits[x]) + int(digits[x + 1])
        x += 1
        print(y)
    print(y)

sum_of_digits()
