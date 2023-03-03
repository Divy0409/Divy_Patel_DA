"""

    For Loop:

    In C,C++ or Java , the syntax of for loop is

    for(i=0;i<10;i++)
    {
        statement
    }

    In Python the for loop syntax is changed drastically.

    syntax :

            for variable-name in range(start-value,end-value,updation):
                statement

            e.g

                for i in range(1,10,1):
                    statement

            i -> variable-name
            range -> Inbuilt function in Python

            range() have 3 parameters

            1) Start Value
            2) End Value
            3) Updation   (increment/decrement)


        for i in range(10):
            print(i)
                
    4 Variants of For Loop.

    - By Default the Loop will start from 0,if you do not
      provide the start value.
    - By Default the Incremented value is +1, if you do not
      provide the updation.

1st Variant

for i in range(10):
    print(i)



#2nd Variant

for i in range(1,10):
    print(i)


#3rd Variant

for i in range(18,47,2):
    print(i)


#4th Variant

for i in range(20,0,-1):
    print(i)
    
"""

n = int(input("Enter No."))
sum=0
for i in range(1,n+1):
    sum=sum+i
    n=n-1

print("Sum : ",sum)


























































