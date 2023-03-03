print("Welcome to Kalyan Jwellers")
name = input("Enter your name: ")
gender = input("Enter your gender m for male and f for female: ")
age = int(input("Enter your age:"))

jwellery = {"ring","bengles","chain","bracelet"}

choice = input("Enter your choosen jwellery: ")
weight = int(input("Enter weight of jwellery: "))

gold_price_mg = int(5752)
making_charge_mg = int(845)
total_cost_gold = (gold_price_mg*weight)
total_cost_making = (making_charge_mg*weight)


if gender == 'm' or gender == 'M':
    if age < 65:
        for total_cost_gold in range(21000,31000):
            actual_cost = (total_cost_gold*0.9)
        for total_cost_gold in range(31000,51000):
            actual_cost = (total_cost_gold*0.8)
        for total_cost_gold in range(51000,999999):
            actual_cost = (total_cost_gold*0.75)

    elif age > 65:
        for total_cost_gold in range(21000,31000):
            actual_cost = (total_cost_gold*0.8)
        for total_cost_gold in range(31000,51000):
            actual_cost = (total_cost_gold*0.7)
        for total_cost_gold in range(51000,999999):
            actual_cost = (total_cost_gold*0.65)

if gender == 'f' or gender == 'F':
    if age < 65:
        for total_cost_gold in range(21000,31000):
            actual_cost = (total_cost_gold*0.85)
        for total_cost_gold in range(31000,51000):
            actual_cost = (total_cost_gold*0.75)
        for total_cost_gold in range(51000,9999999999):
            actual_cost = (total_cost_gold*0.7)

    elif age > 65:
        for total_cost_gold in range(21000,31000):
            actual_cost = (total_cost_gold*0.75)
        for total_cost_gold in range(31000,51000):
            actual_cost = (total_cost_gold*0.65)
        for total_cost_gold in range(51000,9999999999):
            actual_cost = (total_cost_gold*0.6)

total_net_amount = (actual_cost + total_cost_making)
print(total_net_amount)