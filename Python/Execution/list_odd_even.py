
odd_lst = []
even_lst = []
sum = 0

print("Enter numbers to split them in odd and even elements..")

for i in range(0, 4):
    a = int(input("Enter number: "))

    if a % 2 != 0:
        odd_lst.append(a)
        print("Odd list: ", odd_lst)

    else:
        even_lst.append(a)
        print("Even list: ", even_lst)
