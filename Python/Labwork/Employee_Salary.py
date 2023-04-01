Employees = {

    'Abc': {'salary': 30000, 'position': 'Web developer', 'department': 'python'},
    'Pqr': {'salary': 70000, 'position': 'Backend developer', 'department': 'python'},
    'Xyz': {'salary': 40000, 'position': 'Frontend developer','department':'php'}

}

menu = """
    press 1 for updating data
    press 2 for accessing data


"""
print("Original salary , position and department list of employees: ")
print(Employees)

# status = True
# while(status):


A_salary = Employees['Abc']['salary']
P_salary = Employees['Pqr']['salary']
X_salary = Employees['Xyz']['salary']
GA_salary = (1.15*(A_salary))
GP_salary = (1.15*(P_salary))
GX_salary = (1.15*(X_salary))

if A_salary > P_salary and A_salary > X_salary:
    print("Salary of Abc: ",GA_salary)
    Employees['Abc']['salary'] = GA_salary
    
else:
    print("Salary of Abc: ",A_salary)
    
if P_salary > A_salary and P_salary > X_salary:
    print("Salary of Pqr: ",GP_salary)
    Employees['Pqr']['salary'] = GP_salary
else:
    print("Salary of Pqr: ",P_salary)

if X_salary > A_salary and X_salary > P_salary:
      print("Salary of Xyz: ",GX_salary)
      Employees['Xyz']['salary'] = GX_salary
else:
    print("Salary of Xyz: ",X_salary)

print("Gross salary , position and department list of employees: ")
print(Employees)




E_name = input("Enter the name of employee: ")

if E_name in Employees:
    n = Employees[E_name]['salary']
    p = Employees[E_name]['position']
    d = Employees[E_name]['department']
    print("Gross salary: ",n)
    print("Position: ",p)
    print("Department: ",d)


E_position = input("Enter position: ")

A_position = Employees['Abc']['position']
P_position = Employees['Pqr']['position']
X_position = Employees['Xyz']['position']

if E_position == A_position:
    print("Employee name: ",Employees['Abc'])

elif E_position == P_position:
    print("Employee name: ",Employees['Pqr'])

else:
    print("Employee name: ",Employees['Xyz'])

E_department = input("Enter department: ")
A_department = Employees['Abc']['department']
P_department = Employees['Pqr']['department']
X_department = Employees['Xyz']['department']


if E_department == A_department:
    print("Employee name: ",Employees['Abc'])

if E_department == P_department:
    print("Employee name: ",Employees['Pqr'])

if E_department == X_department:
    print("Employee name: ",Employees['Xyz'])