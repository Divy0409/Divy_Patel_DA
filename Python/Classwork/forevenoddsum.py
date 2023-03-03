
n = int(input("Enter Number "))
evensum=0
oddsum=0

for i in range(1,n+1):
    #print(i)
    if i%2==0:
        print("Even : ",i)
        evensum = evensum+i
    else:
        print("Odd : ",i)
        oddsum = oddsum+i

print("Sum of Even Nos. : ",evensum)
print("Sum of Odd Nos. : ",oddsum)


    
