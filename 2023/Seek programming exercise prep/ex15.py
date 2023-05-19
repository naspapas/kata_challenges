def cellphoneBill(duration):
    if duration < 500:
        charge = 0.01
    elif duration > 500 and duration < 800:
        charge = 0.008
    else:
        charge = 0.005

    totalbill = duration * charge
    print(f"Your total bill is {totalbill}. You spoke for {duration} seconds at a rate of ${charge} per second")

cellphoneBill(50000)