product_menu = {
    'Apples' : {'qty' : 12,'amount': 250} ,
    'Kiwi' : {'qty' : 12,'amount': 270},
    'Grapes' : {'qty' : 12,'amount': 190}
}

menu = """

    press 1 for product manager
    press 2 for customer
    press 3 for exit
    
"""
status = True
p_status = True
while status:
    print(menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        while p_status:
            spec = {}
            print("Welcome to Product Manager")
            product_name = input("Enter product name: ")
            qty = int(input("Enter qty: "))
            amount = int(input("Enter amount: "))

            if product_name in product_menu.keys():
                spec['qty'] = product_menu[product_name]['qty'] + qty
                spec['amount'] = amount
            else:
                spec['qty'] = qty
                spec['amount'] = amount

            product_menu[product_name] = spec

            print(product_menu)

            p_choice = input("Do you want to add more: ")
            if p_choice == 'n':
                p_status = False
   
    elif choice == 2:
        print("Product Menu:")
        for k,v in product_menu.items():
            print(f"{k}  {v}")

        cart = {}

        status = True
        while status:
            product_name = input("enter product name:")
            qty_Cart = int(input("eneter qty: "))
            
            n = product_menu[product_name]['qty']
           
            if qty_Cart > n:
                print("Cart exceeds Storage..")

            else:
                price = qty_Cart*product_menu[product_name]['amount']
                print(price)
                cart[product_name] = price
                Remaining_stock = n - qty_Cart
                product_menu[product_name]['qty'] = Remaining_stock
                print(product_menu)

            choice = input("do you want to prurchase more prodect: press y for yes and press n for no")
            if choice == 'n' or choice=='N':
                status=False
                print(cart)   

            

    else:
        print("Thank you for using this application")
        status = False