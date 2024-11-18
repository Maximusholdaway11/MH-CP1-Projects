#Max Holdaway Tic Tac Toe Game

import random as random

print("This is a tic tac toe game. You are x and the computer is o. Spaces 1-9 go from top left to bottom right.")

Space1 = "Empty"

Space2 = "Empty"

Space3 = "Empty"

Space4 = "Empty"

Space5 = "Empty"

Space6 = "Empty"

Space7 = "Empty"

Space8 = "Empty"

Space9 = "Empty"

TicBoard1 = [Space1, Space2, Space3]
TicBoard2 = [Space4, Space5, Space6]
TicBoard3 = [Space7, Space8, Space9]

TicBoard = [TicBoard1, 
            TicBoard2,
            TicBoard3]

SomeoneHasWon = False

while SomeoneHasWon == False:
    RandomChoiceList = [random.choice(TicBoard1), random.choice(TicBoard2), random.choice(TicBoard3)]

    ComputerChoice = random.choice(RandomChoiceList)
    
    if ComputerChoice in [Space1]:
        if Space1 in ["X"]:
            continue
        elif Space1 in ["O"]:
            continue
        elif Space1 in ["Empty"]:
            Space1 = "O"

    if Space1 and Space2 and Space3 in ["O"]:
        SomeoneHasWon = True
        print("The computer has won!")
    elif Space4 and Space5 and Space6 in ["O"]:
        SomeoneHasWon = True
        print("The computer has won!")
    elif Space7 and Space8 and Space9 in ["O"]:
        SomeoneHasWon = True
        print("The computer has won!")
    elif Space1 and Space4 and Space7 in ["O"]:
        SomeoneHasWon = True
        print("The computer has won!")
    elif Space2 and Space5 and Space8 in ["O"]:
        SomeoneHasWon = True
        print("The computer has won!")
    elif Space3 and Space6 and Space9 in ["O"]:
        SomeoneHasWon = True
        print("The computer has won!")
    elif Space1 and Space5 and Space9 in ["O"]:
        SomeoneHasWon = True
        print("The computer has won!")
    elif Space3 and Space5 and Space7 in ["O"]:
        SomeoneHasWon = True
        print("The computer has won!")
    elif Space1 and Space2 and Space3 in ["X"]:
        SomeoneHasWon = True
        print("You have won!")
    elif Space4 and Space5 and Space6 in ["X"]:
        SomeoneHasWon = True
        print("You have won!")
    elif Space7 and Space8 and Space9 in ["X"]:
        SomeoneHasWon = True
        print("You have won!")
    elif Space1 and Space4 and Space7 in ["X"]:
        SomeoneHasWon = True
        print("You have won!")
    elif Space2 and Space5 and Space8 in ["X"]:
        SomeoneHasWon = True
        print("You have won!")
    elif Space3 and Space6 and Space9 in ["X"]:
        SomeoneHasWon = True
        print("You have won!")
    elif Space1 and Space5 and Space9 in ["X"]:
        SomeoneHasWon = True
        print("You have won!")
    elif Space3 and Space5 and Space7 in ["X"]:
        SomeoneHasWon = True
        print("You have won!")
    
    for x in TicBoard:
        print(x)
    ChoiceOfSpace = int(input("Please choose a space to put an x in (Type numbers 1-9):"))
    if ChoiceOfSpace == 1:
        if Space1 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
            continue
        elif Space1 in ["X"]:
            print("You already put something there! Please try again.")
            continue
        elif Space1 in ["Empty"]:
            Space1 = "X"
            print("You have put an X in spot one!")
    elif ChoiceOfSpace == 2:
        if Space2 not in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
            continue
        elif Space2 in ["X"]:
            print("You already put something there! Please try again.")
            continue
        elif Space2 in ["Empty"]:
            Space2 = "X"
    elif ChoiceOfSpace == 3:
        if Space3 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
            continue
        elif Space3 in ["X"]:
            print("You already put something there! Please try again.")
            continue
        elif Space3 in ["Empty"]:
            Space3 = "X"