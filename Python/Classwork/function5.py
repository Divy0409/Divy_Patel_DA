db = {} #blank dictionary

def registration(firstname,email,password): # function with parameters..
    db['name'] = firstname
    db['email'] = email
    db['password'] = password
    print("Registartion successfully...")

def login(email,password):
    if email == db['email']:
    
        if password == db['password']:
            return db['name']
        
        else:
            return "Invalid Email or Password"
        
    else:
        return "Inavlid email or password"
    
status = True
while status:

    menu = """
            1) press 1 for registration
            2) press 2 for login
            3) press 3 for exit
    """
    print(menu)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        registration(name,email,password)

    elif choice == 2:
        email = input("Enter email: ")
        password = input("Enter password: ")

        print(login(email,password))

    elif choice == 3:
        status = False