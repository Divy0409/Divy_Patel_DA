import math

a = int(input("Eneter number 1: "))
b = int(input("Enter number 2: "))
c = math.gcd(a,b)
print(c)

# def hcf(a, b):
#     if(b == 0):
#         return a
#     else:
#         return hcf(b, a % b)
 
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# print("The gcd of two numbers is : ", end="")
# print(hcf(a,b))