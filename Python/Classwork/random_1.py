import random

random_number = random.randint(1,100)
print(random_number)
random_float = random.random() #*100
print(random_float)

lst = ["Python","Java","Html","Javascript"]
choice = random.choice(lst)
print(choice)
print(lst.count("Java"))

t = ("Python","Java","Html","Javascript")
l1 = list(t)
l1[0] = "Flatter"
t = tuple(l1)
print(t)
