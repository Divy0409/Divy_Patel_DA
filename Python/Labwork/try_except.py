print("Enter number1:")
num1 = int(input())
print("Enter number2:")
num2 = int(input())

try:
    print("The sum of two number is:", int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very Important")    
