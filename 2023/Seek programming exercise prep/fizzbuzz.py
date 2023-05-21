def fizzbuzz():
    fizzbuzzAmount = int(input("Please enter number you would like to count to: "))
    x = 1

    for x in range(1, fizzbuzzAmount):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 == 0:
            print("Fizz")
        else:
            print(x)
        


fizzbuzz()
    