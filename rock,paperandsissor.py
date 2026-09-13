import random

choices = ["rock" , "paper" , "sissor" ]

computer = random.choice(choices)

user = input("Enter rock , paper or sissor : ").lower()

print("Computer choose :", computer) 

if(computer == user):
    print("Its a tie!")
elif(user == "rock"):
    if(computer == "paper"):
        print("U lose")
    else:
        print("U win")
elif(user == "paper"):
    if(computer == "sissor"):
        print("U lose")
    else:
        print("U win")
elif(user == "sissor"):
    if(computer== "rock"):
        print("U lose")
    else:
        print("U win")
else:
    print("U input invalid option , please choose from rock,paper or sissor ")

print("End of game , Thank you!")