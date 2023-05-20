def calculate_user_sum():
    desiredNumber = input("To what number would you like to calculate? ")
    total = 0
    averageCounter = 0
    for sum in range(1, int(desiredNumber) + 1):
        total += sum
        averageCounter += 1
    total /= averageCounter
    print(total)

calculate_user_sum()