def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("Enter the number: "))
print("Factorial using iterative method ",factorial_iterative(number))

def factorial_recursive(n):
    if n == 1:
        return 1
    
    else:
        return n * factorial_recursive(n-1)
    
print("Factorial using recursive method ",factorial_recursive(number))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(number))
