n = 18
ch = 8 #here total choices will be 9 because intially ch will not be decremented
while(True):
    i=int(input("enter your choosen number :"))
    if i<n and ch!=0:
        print("your entered choice is smaller")
        print("no. of choices left", ch)
        ch = ch-1
        continue
    elif i>n and ch!=0:
        print("your entered choice is greater")
        print("no. of choices left", ch)
        ch = ch-1
        continue
    elif i==n and ch!=0:
        print("you won")
        print("you completed it in",ch,"choices")
        break
    elif ch==0:
        print("you lost try again")
        break