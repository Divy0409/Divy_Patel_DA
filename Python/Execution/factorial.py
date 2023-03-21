def fact_fun(n):
    fact = 1
    for i in range(n):
        fact = fact*(i+1)
        print("fact", fact)

    return fact


n = int(input("Enter number:"))

print(fact_fun(n))
