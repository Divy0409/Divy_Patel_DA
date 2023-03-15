import random

print("Welcome to IPL..")
Team_List = ["CSK","MI","KKR","RR","RCB"]

Team_1 = input("Enter your choosen team: ")
Team_List.remove(Team_1)

print("Opponents: ",Team_List)
choice = random.choice(Team_List)
print("Next match vs ",choice)

print("Welcome to matchday of..")
print(Team_1+ " vs " +choice)

print("Toss time..")
Toss = ["Heads","Tails"]
Decision = ["Bat","Boll"]

Toss_result = random.choice(Toss)
Toss_choice = input("Enter your toss prediction: ")

if Toss_choice == Toss_result:
    print("You won the Toss..")
    Toss_decision = input("Enter your decision: ")
    print("You choosen: ",Toss_decision)
    
else:
    print("Opponent won the Toss..")
    random_decision = random.choice(Decision)
    print("Opponent choosen: ",random_decision)

    