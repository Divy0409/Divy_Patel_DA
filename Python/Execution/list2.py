lst = []
sum=0

print("Enter numbers to get avg..")

for i in range(0,10):
    a = int(input("Enter number: "))
    lst.append(a)
    print(lst)

lst.sort()
print(lst)
print("minimum num: ",lst[0])
print("maximum num: ",lst[3])

for i in lst:

    sum = sum+i
    
avg = (sum/10)
print(avg)