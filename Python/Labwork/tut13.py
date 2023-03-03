# var1 = 6
# var2 = 56
# var3 = int(input())
# if var3>var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")
# list1 = [5,7,3]
# # if 5 in list1:
# #     print("yes it is")
# print(15 not in list1)
#  if 15 not in list1:
#      print("no  it is not in the list")

var1 = 18
print("enter your age")
var2 = int(input())
if var2>7 and var2<100:
    if var2<var1:
        print("you are not eligiable for driving the car")
    elif var2>var1:
        print("you are eligiable for driving the car")
    elif var2==var1:
        print("you have to give driving test")
else:
    print("Enter valid age")