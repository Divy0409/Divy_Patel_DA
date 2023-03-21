n = 5

print("Pattern 1: ")
for i in range(0, n):
    print()
    for j in range(0, i):
        print("*", end=" ")
    print()

print("Pattern 2: ")
for i in range(n, 0, -1,):
    print()
    for j in range(0, i):
        print("*", end=" ")
    print()

print("Pattern 3: ")
for i in range(0, n):
    print(" "*(n-i), " *"*i)

print("Pattern 4: ")
for i in range(n, 0, -1):
    print(" "*(n-i), " *"*i)


print("Pattern 5: ")
for i in range(0, n):
    print(" "*(n-i), " *"*i)

for i in range(n, 0, -1):
    print(" "*(n-i), " *"*i)
