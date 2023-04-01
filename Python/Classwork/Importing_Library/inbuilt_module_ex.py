import math
# factorial of number:

# take one variable which contain one value
f=1

# accept number fromm user
num = int(input("Enter num : "))

# continous multiplication of num with f value
for i in range(1,num+1): # num = 5 (1,6)
    f *= i

print(f)

# fac using library
f = math.factorial(num)
print(f)