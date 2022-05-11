f = open("input1.txt", "r")
check = []
n = 0
amount = 0
for x in f:
    check.append(x)

for x in check:
    try:
        if (int(check[n]) + int(check[n + 1]) + int(check[n + 2]))  < (int(check[n + 1]) + int(check[n + 2]) + int(check[n + 3]):
            amount += 1
    except:
        pass
    n += 1

print(amount)
f.close()
