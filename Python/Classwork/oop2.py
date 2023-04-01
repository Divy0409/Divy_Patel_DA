# class define for student
class student:
    # dictionary - we use as a database 
    db = {}

    # input method - which accept value fom student user
    def input(self): # self is used to access class properties

        email = input("Enter email: ")
        password = input("Enter password: ")
        # storing data in db

        # here email is key and password is value
        self.db[email] = password

    def display(self):
        # display all students
        for k in self.db.keys():
            print("email = ",k)
class faculty:
    # dictionary - we use as a database 
    db = {}

    # input method - which accept value fom student user
    def input(self): # self is used to access class properties

        email = input("Enter email: ")
        password = input("Enter password: ")
        # storing data in db

        # here email is key and password is value
        self.db[email] = password

    def display(self):
        # display all students
        for k in self.db.keys():
            print("email = ",k)

# object creation of student class
s1 = student()
s2 = faculty()
status = True
while status:
    # menu
    data = """
            press 1 for student registration
            press 2 for faculty registration
            press 3 for view all students
            press 4 for view all faculties
            press 5 for exit
    """
    print(data)
    user_input = int(input("Enter your choice : "))
    if user_input==1:
        s1.input()
    elif user_input==2:
        s2.input()
    elif user_input==3:
        s1.display()
    elif user_input==4:
        s2.display()
    else:
        status = False
    choice = input("Do you want to add more operations(y/n): ")
    if choice == 'n':
        status = False

