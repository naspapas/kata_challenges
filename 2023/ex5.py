import math
money = 100
banana_price = 2
apple_price = 3
kiwi_price = 4

buyable_bananas = math.floor(money / banana_price)
buyable_apples = math.floor(money / apple_price)
buyable_kiwi = math.floor(money / kiwi_price)
print(f"You can buy {buyable_bananas} bananas")
print(f"You can buy {buyable_apples} apples")
print(f"You can buy {buyable_kiwi} kiwis")