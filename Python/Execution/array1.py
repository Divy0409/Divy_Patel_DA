def ocr(n, x):

    ocr_ele = 0
    for i in x:
        if i == n:
            ocr_ele = ocr_ele+1

    return ocr_ele


x = [1, 2, 3]

# n = int(input("Enter element: "))
# x.append(n)

print(x)

# x.reverse()
# print(x)

# i = int(input("Enter index of element you want to remove: "))
# x.pop(i)
# print(x)

n = int(input("Enter element to know its occurance:"))
y = ocr(n, x)
print(y)
