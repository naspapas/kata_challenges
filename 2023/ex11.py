hourly_income = 4
hours_worked = 50
total_money = hourly_income * hours_worked

def calculate(total_money):
    ps4cost = 200
    phonecost = 900
    tvcost = 500
    gameskincost = 9.99
    
    purchaseps4 = total_money // ps4cost
    purchasephone = total_money // phonecost
    purchasetv = total_money // tvcost
    purchasegameskin = total_money // gameskincost
    print(f"I can buy {purchaseps4} PS4's, {purchasephone} phone's, {purchasegameskin} skins, or {purchasetv} tv's" )

calculate(total_money)



