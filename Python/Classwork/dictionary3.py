jay_bhavani = {
    "vadapav" : 30,
    "dabeli" : 20,
    "bhel" : 70,
}

print("menu")
for k,v in jay_bhavani.items():
    print(f"{k} Rs. {v}")

cart = {}

status = True
while status:
    product_name = input("enter product name:")
    qty = int(input("eneter qty: "))

    price = qty*jay_bhavani[product_name]
    print(price)

    cart[product_name] = price

    choice = input("do you want to prurchase more prodect: press y for yes and press n for no")
    if choice == 'n' or choice=='N':
        status=False
        print(cart)