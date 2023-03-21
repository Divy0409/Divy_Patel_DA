lst = []
mul = 1

print("Enter your SPI..")

for i in range(0, 4):
    a = int(input("Enter Your spi: "))
    lst.append(a)
    print(lst)

lst.sort()
print(lst)
print("minimum spi: ", lst[0])
print("maximum spi: ", lst[3])

for i in lst:

    mul = mul*i

print(mul)
