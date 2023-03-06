#health management system

def getdate():
    import datetime
    return datetime.datetime.now()

def take(k):
    
    if(k == 1):
        c = int(input("Enter 1 for exercise and 2 for food: "))
        
        if(c == 1):
            value = input("Enter exercise: ")
            with open("abc.txt","a") as ab:
                ab.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully updated!!")

        elif(c == 2):
            value = input("Enter food: ")
            with open("abc1.txt","a") as ab:
                ab.write(str([str(getdate())])+":"+value+"\n")
            print("Successfully updated!!")
    
    elif(k == 2):
        c = int(input("Enter 1 for exercise and 2 for food: "))
        
        if(c == 1):
            value = input("Enter exercise: ")
            with open("pqr.txt","a") as ab:
                ab.write(str([str(getdate())])+":"+value+"\n")
            print("Successfully updated!!")

        elif(c == 2):
            value = input("Enter food: ")
            with open("pqr1.txt","a") as ab:
                ab.write(str([str(getdate())])+":"+value+"\n")
            print("Successfully updated!!")
    
    elif(k == 3):
        c = int(input("Enter 1 for exercise and 2 for food: "))
        
        if(c == 1):
            value = input("Enter exercise: ")
            with open("xyz.txt","a") as ab:
                ab.write(str([str(getdate())])+":"+value+"\n")
            print("Successfully updated!!")

        elif(c == 2):
            value = input("Enter food: ")
            with open("xyz1.txt","a") as ab:
                ab.write(str([str(getdate())])+":"+value+"\n")
            print("Successfully updated!!")

    else:
        print("User not found: ")
    
def retrieve(k):
    
    if(k == 1):
        c = int(input("Enter 1 for exercise and 2 for food: "))

        if(c == 1):
            with open("abc.txt") as ab:
                for i in ab:
                    print(i,end="")

        elif(c == 2):
            with open("abc1.txt") as ab:
                for i in ab:
                    print(i,end="")
            
    elif(k == 2):
        c = int(input("Enter 1 for exercise and 2 for food: "))

        if(c == 1):
            with open("pqr.txt") as ab:
                for i in ab:
                    print(i,end="")

        elif(c == 2):
            with open("pqr1.txt") as ab:
                for i in ab:
                    print(i,end="")

    elif(k == 3):
        c = int(input("Enter 1 for exercise and 2 for food: "))

        if(c == 1):
            with open("xyz.txt") as ab:
                for i in ab:
                    print(i,end="")

        elif(c == 2):
            with open("xyz1.txt") as ab:
                for i in ab:
                    print(i,end="")

    else:
        print("User not found: ")
    
print("Welcome to Health Management System: ")
a = int(input("Press 1 for log and 2 for retrival: "))

if a == 1:
    b = int(input("Enter 1 for abc 2 for pqr 3 or xyz: "))
    take(b)

elif a == 2:
    b = int(input("Enter 1 for abc 2 for pqr 3 or xyz: "))
    retrieve(b)
