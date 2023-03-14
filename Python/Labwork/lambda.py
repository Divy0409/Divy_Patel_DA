# # Lambda functions or anonymous functions
# def add(a,b):
#     return a + b

# minus = lambda x,y: x-y

# # def minus(x,y):
# #     return x-y

# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# print("Subtraction of two numbers is: ",minus(num1,num2))
#--------------------------------------------------------------------------------------

# def a_first(a):
#     return a[1]

a = [[1,14],[5,6],[8,23]]
#a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)