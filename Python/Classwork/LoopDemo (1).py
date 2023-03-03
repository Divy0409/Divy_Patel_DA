"""
    Loop : It is continously repeating the same task again and again is
           called a loop.

    In Python,

    There are 2 Loops

    1) while loop
    2) for loop

    Every Loop will have 3 common facts

    1) Initialization
    2) Conditional
    3) Updation (increment/decrement)



    a) while

    syntax:
                initialization
                while condition:
                    statement
                    updation 



#Program 1

n = int(input("Enter No."))

while n>0:
    print("Tops Tech")    
    n = n-1


#WAP to print the no. from 1 to 20

n = 1
while n<=20:
    print(n)
    n = n+1
    
"""
#WAP to print the sum of No.s

n = int(input("Enter N : "))
sum=0

while n>0:    
    sum = sum+n
    n = n-1

print("Sum ",sum)































