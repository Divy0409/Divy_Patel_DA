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

# object creation of student class
s1 = student()
status = True
while status:
    s1.input()
    choice = input("Do you want to add more students(y/n): ")
    if choice == 'n':
        status = False
        s1.display()