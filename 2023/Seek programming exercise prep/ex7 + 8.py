years = 5
children = 3
minwage = 400
missed_days = 0

total = (years * 20) + (children * 30) + minwage
if missed_days == 0:
    total += 100
print(total)