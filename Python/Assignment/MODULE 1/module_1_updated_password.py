import random
import array
 
db = {} #blank dictionary

def Creat_Pass(firstname,password): # function with parameters..
    db['name'] = firstname
    db['password'] = password
    print("Password created successfully...")

def Access_Pass(name):
    if name == db['name']:
        return db['password']
               
    else:
        return "User not found.."
    
status = True
while status:

    menu = """
            1) press 1 for creating Password
            2) press 2 for accessing Password
            3) press 3 for exit
    """
    print(menu)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter name: ")
    
        MAX_LEN = 8

        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']
        
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']
        
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']

        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
        
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
        
        password = ""
        for x in temp_pass_list:
                password = password + x
                
        print(password)

        Creat_Pass(name,password)

    elif choice == 2:
        name = input("Enter name: ")
        print(Access_Pass(name))

    elif choice == 3:
        status = False