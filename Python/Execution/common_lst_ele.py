lst1 = []
lst2 = []


print("Enter lst1 elements..")

for i in range(0, 4):
    a = int(input("Enter number: "))
    lst1.append(a)
    print(lst1)

print("Enter lst2 elements..")

for i in range(0, 4):
    b = int(input("Enter number: "))
    lst2.append(b)
    print(lst2)


def common_ele(lst1, lst2):
    lst1_ele = set(lst1)
    lst2_ele = set(lst2)

    if (lst1_ele & lst2_ele):
        print("Same elements..", lst1_ele & lst2_ele)

    else:
        print("No same elements found..")


print(lst1)
print(lst2)
common_ele(lst1, lst2)
lst3 = []

for i in lst1:
    if i in lst2:
        lst3.append(i)
print(lst3)
