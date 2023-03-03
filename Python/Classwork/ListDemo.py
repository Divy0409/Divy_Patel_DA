"""
    List  : It is a group of Data, which contains multiple types
            of values.

            - Duplicate Values are allowed.
            - Insertion Order is Maintained.
            - Indexing starts with 0.

            -In Python, list is used with []    
"""

l = [1,2,3,1.1,2.2,3.1,"Python",False,0,1,True,0,"Tops"]
print(l)

l.append(100)
print(l)

l1 = l.copy()
print(l1)

l2 = l.copy()
print(l2)

l1.append(200)
print(l1)

l2.append(300)
print(l2)

print(l.count(0))
print(l.count(1))

l.pop()
print(l)
l.pop()
print(l)

l3 = [1001,1002,1003]
l.extend(l3)
print(l)
print(l.index(1001))
l.insert(6,"Avadh")
print(l)
l.remove(1.1)
print(l)
l.reverse()
print(l)

for i in l:
    print(i)
    
print("Python" in l)











