try:
    #accept numbers
    num1= int(input("Enter Number 1: "))
    num2= int(input("Enter Number 2: "))

    #calculation
    ans =num1/num2

    #display answer
    print(ans)

except ValueError:
    print("Invalid Input -  only 0-9 required")
except ZeroDivisionError:
    print("Can not be devided by zero")
except:
    print("Invalid input")