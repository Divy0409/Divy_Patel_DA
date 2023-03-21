import math

me = 1
a = "this is %s"%me
print(a)

b = "xyz"
a1 = 3
# c = "this is %s %s"%(me,a1)
# c = "This is {1} {0}"
# d = c.format(b,a1)
# print(d)

a2 = f"this is {b} {a1} {4*65} {math.cos(65)}"
print(a2)