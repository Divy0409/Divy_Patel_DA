n = int(input("Enter the the number of rows:"))
a = int(input("Enter 0 or 1: "))
b = bool(a)

if b == True:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()

if b == False:
    for i in range(n,0,-1,):
        for j in range(1,i+1):
            print("*",end="")
        print()