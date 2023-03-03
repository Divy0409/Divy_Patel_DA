n1=int(input("enter the A: "))
n2=int(input("enter the B: "))
n3=int(input("enter the C: "))
print("A = ",n1,"B = ",n2,"C = ",n3)
if n1>n2:
    if n1>n3:
        print(n1," is max")
    else:
        print(n3," is max")    
else:
     if n2>n3:
        print(n2," is max")
     else:
        print(n3," is max")