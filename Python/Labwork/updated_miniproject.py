print("Welcome to Kalyan Jwellers")
name = input("Enter your name: ")
gender = input("Enter your gender m for male and f for female: ")
age = int(input("Enter your age:"))

jwellery = ['ring','bengles','chain','bracelet','Ring','Bengles','Chain','Bracelet']

choice = input("Enter your choosen jwellery: ")


if choice in jwellery:

    weight = int(input("Enter weight of jwellery: "))
    gold_price_mg = int(5752)
    making_charge_mg = int(845)
    total_cost_gold = (gold_price_mg*weight)
    total_cost_making = (making_charge_mg*weight)

    if gender == 'm' or gender == 'M':
        if age < 65:
            for total_cost_gold in range(0,20999):
                actual_cost = (total_cost_gold*1.0)
            for total_cost_gold in range(21000,30999):
                actual_cost = (total_cost_gold*0.9)
            for total_cost_gold in range(31000,50999):
                actual_cost = (total_cost_gold*0.8)
            for total_cost_gold in range(51000,999999):
                actual_cost = (total_cost_gold*0.75)

        elif age > 65:
            for total_cost_gold in range(0,20999):
                actual_cost = (total_cost_gold*1.0)
            for total_cost_gold in range(21000,30999):
                actual_cost = (total_cost_gold*0.8)
            for total_cost_gold in range(31000,50999):
                actual_cost = (total_cost_gold*0.7)
            for total_cost_gold in range(51000,999999):
                actual_cost = (total_cost_gold*0.65)

    elif gender == 'f' or gender == 'F':
        if age < 65:
            for total_cost_gold in range(0,20999):
                actual_cost = (total_cost_gold*1.0)
            for total_cost_gold in range(21000,30999):
                actual_cost = (total_cost_gold*0.85)
            for total_cost_gold in range(31000,50999):
                actual_cost = (total_cost_gold*0.75)
            for total_cost_gold in range(51000,999999):
                actual_cost = (total_cost_gold*0.7)

        elif age > 65:
            for total_cost_gold in range(0,20999):
                actual_cost = (total_cost_gold*1.0)
            for total_cost_gold in range(21000,30999):
                actual_cost = (total_cost_gold*0.75)
            for total_cost_gold in range(31000,50999):
                actual_cost = (total_cost_gold*0.65)
            for total_cost_gold in range(51000,999999):
                actual_cost = (total_cost_gold*0.6)



    total_net_amount = (actual_cost + total_cost_making)
    print("Your grand total: ")
    print(total_net_amount)

    if age < 18 :
        if gender == 'm':
            print("Thank you for shopping Mr."+name)
        else:
            print("Thank you for shopping Miss "+name)

    elif age > 18:
        if gender == 'm':
            print("Thank you for shopping Mr."+name)
        else:
            print("Thank you for shopping Ms."+name)

else:
    print("No such jwellery available.")

