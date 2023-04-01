# list define
l1 = [12,13,14,15,16,17]

try:
    # access specific element from the list
    n = int(input("Enter index to get specific element: "))
    print(l1[n])
except ValueError:
    print("Enter only numbers..")

except:
    print("List index out of bound.")
else:
    # display list
    print(l1)