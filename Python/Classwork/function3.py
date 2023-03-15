def even_odd():
    if num%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

def pos_neg():
    if num>0:
        print("Number is positive")
    elif num==0:
        print("zero")
    else:
        print("Number is negative")

num = int(input("Enter the number: "))
even_odd()
pos_neg()