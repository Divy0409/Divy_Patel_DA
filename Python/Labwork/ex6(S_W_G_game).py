import random

n = 0
S_P = 0
U_P = 0
Game = ['snake','water','gun']
print("Game characters: ",Game)

while(n < 10):
    
    
    User_Ch = input("Enter your desired character: ")
    Game_Ch = random.choice(Game)
    print("Game choice: ",Game_Ch)
    print("User choice: ",User_Ch)

    
    if Game_Ch == 'snake' and User_Ch == 'water' :
        print("Point to System..")
        n = n + 1
        S_P = S_P + 1        
        print("Your score: ",U_P)
        print("System score: ",S_P)
        

    elif Game_Ch == 'gun' and User_Ch == 'water' :
        print("Point to User..")
        n = n + 1
        U_P = U_P + 1        
        print("Your score: ",U_P)
        print("System score: ",S_P)
        

    elif Game_Ch == 'gun' and User_Ch == 'sanke' :
        print("Point to System..")
        n = n + 1
        S_P = S_P + 1        
        print("Your score: ",U_P)
        print("System score: ",S_P)
        

    
    elif Game_Ch == 'snake' and User_Ch == 'gun':
        print("Point to User..")
        n = n + 1
        U_P = U_P + 1        
        print("Your score: ",U_P)
        print("System score: ",S_P)
        

    elif Game_Ch == 'water' and User_Ch == 'gun' :
        print("Point to System..")
        n = n + 1
        S_P = S_P + 1 
        print("Your score: ",U_P)
        print("System score: ",S_P)
        

    elif Game_Ch == 'water' and User_Ch == 'snake' :
        print("Point to User..")
        n = n + 1
        U_P = U_P + 1
        print("Your score: ",U_P)
        print("System score: ",S_P)
        

    elif Game_Ch == User_Ch :
        print("Tie..")
        n = n+1   
        print("Your score: ",U_P)
        print("System score: ",S_P)

    else:
        print("Invalid input..")
        
    print("Number of trials left: ",(10-n))    

if S_P > U_P:
    print("You Lost..")

elif S_P == U_P:
    print("Tie no one wins..")

else:
    print("You won..")