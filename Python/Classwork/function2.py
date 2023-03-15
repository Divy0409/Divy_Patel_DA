def addition():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print((num1 + num2))

def multiplication():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print((num1 * num2))

def menu():
    data = """
            Menu

            press 1 for addition
            press 2 for multiplication 
            
            
           """
    print(data)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        addition()
    else:
        multiplication()

menu() #calling


