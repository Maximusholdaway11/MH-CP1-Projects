#Max Holdaway Rock, Paper, Scissors

import random as random

PlayerScore = 0

ComputerScore = 0

GameList = ["Rock", "Paper", "Scissors"]

print("This is a Rock, Paper, Scissors game")

print("")

while True:
    Choice = str(input(""""Please choose which option you want to do
                       To play the game type out Game (FYI Please capitalize the first letter for your choice of Rock, Paper, or Scissors)
                       To check the current scores type Scores
                       To exit the game type out Exit:\n"""))
    if Choice in ["Game", "game"]:
        RockPaperScissorsChoice = str(input("Please tell me if you want to do rock paper or scissors: "))
        ComputerRockPaperScissorsChoice = random.choice(GameList)
        if RockPaperScissorsChoice in ["Rock"] and ComputerRockPaperScissorsChoice in ["Scissors"]:
            print("You have won this round! the computer chose Scissors")
            PlayerScore += 1
        elif RockPaperScissorsChoice in ["Paper"] and ComputerRockPaperScissorsChoice in ["Rock"]:
            print("You have won this round! the computer chose Rock")
            PlayerScore += 1
        elif RockPaperScissorsChoice in ["Scissors"] and ComputerRockPaperScissorsChoice in ["Paper"]:
            print("You have won this round! the computer chose Paper")
            PlayerScore += 1
        elif RockPaperScissorsChoice in ["Rock"] and ComputerRockPaperScissorsChoice in ["Paper"]:
            print("You have lost this round the computer chose Paper")
            ComputerScore += 1
        elif RockPaperScissorsChoice in ["Paper"] and ComputerRockPaperScissorsChoice in ["Scissors"]:
            print("You have lost this round the computer chose Scissors")
            ComputerScore += 1
        elif RockPaperScissorsChoice in ["Scissors"] and ComputerRockPaperScissorsChoice in ["Rock"]:
            print("You have lost this round the computer chose Rock")
            ComputerScore += 1
        elif RockPaperScissorsChoice in ["Rock"] and ComputerRockPaperScissorsChoice in ["Rock"]:
            print("It was a draw! The computer chose Rock")
        elif RockPaperScissorsChoice in ["Paper"] and ComputerRockPaperScissorsChoice in ["Paper"]:
            print("It was a draw! The computer chose Paper")
        elif RockPaperScissorsChoice in ["Scissors"] and ComputerRockPaperScissorsChoice in ["Scissors"]:
            print("It was a draw! The computer chose Scissors")
        else:
            print("Invalid Selection please try again")
            continue
    
    elif Choice in ["Scores", "scores"]:
        if PlayerScore < 1 and ComputerScore < 1:
            print("There aren't any scores yet play a few games and check back later.")
        else:
            print(f"Here are the current scores {PlayerScore}:{ComputerScore} (Your score is first the computers score is second)")

    elif Choice in ["Exit", "exit"]:
        print("Thanks for playing see you later!")
        break

    else:
        print("Error Please try again")