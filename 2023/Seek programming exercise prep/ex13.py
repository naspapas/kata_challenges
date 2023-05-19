def netcafe(isMember, hoursSpent):
    if isMember:
        membershipStatus = "a Member"
        perhourcost = 2
        tax = 0.10
    else:
        membershipStatus = "not a Member"
        perhourcost = 5
        tax = 0.20
    
    cost = perhourcost * hoursSpent
    totalcost = cost + (cost * tax)

    print(f"The user is {membershipStatus}. They stayed for {hoursSpent} hours, with an hourly cost of {perhourcost}$ and {tax * 100}% tax. The total cost owed is {totalcost}$.")

netcafe(False, 10.5)