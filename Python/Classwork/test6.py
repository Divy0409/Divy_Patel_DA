roll=int(input("enter the rollno: "))
name=input("enter the name: ")
p=int(input("enter the physics marks: "))
c=int(input("enter the chemistry marks: "))
m=int(input("enter the maths marks: "))
total = (p+c+m)
per = (total/3)
print("*"*80)
print()
print("Rollno = ",roll)
print("Name = ",name)
print("Totel = ",total)
print("Percentage = ",per)

if per>75:
   print("distinction class")
elif per>60:
   print("First class")
elif per>50:
   print("second class")
elif per>40:
   print("pass class")
else:
   print("Fail!")            