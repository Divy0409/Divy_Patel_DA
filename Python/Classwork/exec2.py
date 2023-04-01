try:
    #accept numbers
    num1= int(input("Enter Number 1: "))
    num2= int(input("Enter Number 2: "))

    #calculation
    ans =num1/num2

    #display answer
    print(ans)

except:
    print("Invalid Input.")

else:
   # It is always executable....
    print("Welcome to math world.")

finally:
    print("Thank you for using application.")