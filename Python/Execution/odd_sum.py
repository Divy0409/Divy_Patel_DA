n = int(input("Enter a number: "))

sum = 0

for i in range(0, n):
    if i % 2 != 0:
        sum = sum+i

print(sum)
