# i=0
# while(True):
#     if i+1<5:
#         i=i+1
#         continue
#     print(i+1,end=" ")
#     if(i==44):
#         break
#     i=i+1

while(True):
    i = int(input("enter integer input :"))
    if(i<=100):
        print("try again")
        continue
    else:
        print("congrats value is greater than 100")
        break
