#A Rock paper scissors game

import random

def get_choices(): 
    Player_Choice = input("Enter Rock Paper Scissors: ")
    options = ["Rock","Paper","Scissors"]
    Computer_Choice = random.choice(options)
    choice = {"Player" : Player_Choice, "Computer" : Computer_Choice}
    return choice

def check_win(Player,Computer):
    print(f"Your Choice:{Player} Computer Choice:{Computer}")
    if(Player==Computer):
        return "Its a TIE"
    elif(Player=="Rock"):
        if(Computer=="Paper"):
            return "Paper covers Rock. You lose!"
        else:
            return "Rock smashes Scissors. You win!"
    elif(Player=="Scissors"):
        if(Computer=="Rock"):
            return "Rock smashes Scissors. You lose!"
        else:
            return "Scissors shreds paper. You win!"
    elif (Player=="Paper"):
        if(Computer=="Rock"):
            return "Paper covers rock. You win!"
        else:
            return "Scissors shreds paper. You lose!"
    else:
        print("Invalid choices")

choices = get_choices()
result = check_win(choices["Player"],choices["Computer"])
print(result)
