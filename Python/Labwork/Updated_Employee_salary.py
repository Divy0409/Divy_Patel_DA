Employees = {

    1: {'name': 'Abc', 'salary': 30000, 'G_salary': 30000, 'position': 'Web developer', 'department': 'python'},
    2: {'name': 'Pqr', 'salary': 70000, 'G_salary': 70000, 'position': 'Backend developer', 'department': 'python'},
    3: {'name': 'Xyz', 'salary': 40000, 'G_salary': 40000, 'position': 'Frontend developer', 'department': 'php'}

}

menu = """
    press 1 for updating data
    press 2 for accessing data
    press 3 for exit

"""

status = True
P_status = True
while(status):
    print(menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        while P_status:
            U_Employee = {}
            Employee_id = int(input("Enter employee number: "))
            name = input("Enter employee name: ")
            salary = int(input("Enter employee salary: "))
            position = input("Enter employee position: ")
            department = input("Enter department of employee: ")

            U_Employee['name'] = name
            U_Employee['salary'] = salary
            U_Employee['position'] = position
            U_Employee['department'] = department

            for i in range(1, len(Employees)+1):
                if U_Employee['salary'] > Employees[i]['salary']:
                    G_salary = (1.15*(salary))

                else:
                    G_salary = (1*(salary))

            U_Employee['G_salary'] = G_salary
            Employees[Employee_id] = U_Employee
            print(Employees)

            p_choice = input("Do you want to add more data(y/n): ")
            if p_choice == 'n':
                P_status = False

    elif choice == 2:

        

        # max_s = max([int(i['salary'])for i in Employees.values()])
        # Gr_s = (1.15(max_s))

        # print(max_s)

        
        # for i in range(1, len(Employees)+1):
            
            
        #     if choice == Employees[i]['name']:
        #             print(Employees[i]['G_salary'])
        #             break
            

        # for i in range(1, len(Employees)+1):
        #     T_department = input("Enter employee department: ")
        #     if T_department == Employees[i]['department']:
        #         print(Employees[i]['G_salary'])
        #         break
               

        # for i in range(1, len(Employees)+1):
        #     T_position = input("Enter employee position: ")
        #     if T_position == Employees[i]['position']:
        #         print(Employees[i]['G_salary'])
        #         break

        C_menu = """
                Press 1 for accessing data using name
                Press 2 for accessing data using department
                Press 3 for accessing data using position
        """
        print(C_menu)

        C_choice = int(input("Enteryour choice: "))
        if choice == 1:
            T_name = input("Enter employee name: ")
            for i in  range(1,len(Employees)):
                print(Employees[i][T_name])


        elif choice == 2:
            T_department = input("Enter employee department: ")
            for i in  range(1,len(Employees)):
                print(Employees[i][T_department])


        elif choice == 3:
            T_position = input("Enter employee position: ")
            for i in  range(1,len(Employees)):
                print(Employees[i][T_position])


        
    else:
        status = False