x = [1,2,3]
print(x)
status = True
while(status):
    c = input("Do you want to add more elements(y/n): ")
    if c == 'y':
        a = int(input("Enter element:"))
        x.append(a)
    else:
        status = False

print(x)

x.sort()
y = len(x)
print("No of elements in array",y)

for i in range(1,y-1):
    print(x[i])
