number = int(input("Enter the number: "))
def factorial_recursive(n):
    if n == 1:
        return 1
    
    else:
        return n * factorial_recursive(n-1)
    
print("Factorial using recursive method ",factorial_recursive(number))
