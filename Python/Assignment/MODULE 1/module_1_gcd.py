def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
 
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("The gcd of two numbers is : ", end="")
print(hcf(a,b))