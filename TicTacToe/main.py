#Max Holdaway Tic Tac Toe Game

import random as random

print("This is a tic tac toe game. You are x and the computer is o. Spaces 1-9 go from top left to bottom right.")

Space1 = "Empty1"

Space2 = "Empty2"

Space3 = "Empty3"

Space4 = "Empty4"

Space5 = "Empty5"

Space6 = "Empty6"

Space7 = "Empty7"

Space8 = "Empty8"

Space9 = "Empty9"

TicBoard1 = [Space1, Space2, Space3]
TicBoard2 = [Space4, Space5, Space6]
TicBoard3 = [Space7, Space8, Space9]

TicBoard = [TicBoard1, 
            TicBoard2,
            TicBoard3]

SomeoneHasWon = False

while SomeoneHasWon == False:
    for x in TicBoard:
        TicBoard1 = [Space1, Space2, Space3]
        TicBoard2 = [Space4, Space5, Space6]
        TicBoard3 = [Space7, Space8, Space9]

        TicBoard = [TicBoard1, 
                    TicBoard2,
                    TicBoard3]
        print(x)

    ComputerChoice = random.choice(["Empty1", "Empty2", "Empty3", "Empty4", "Empty5", "Empty6", "Empty7", "Empty8", "Empty9"])

    if ComputerChoice in ["Empty1"]:
        if Space1 in ["X"]:
            pass
        elif Space1 in ["O"]:
            pass
        elif Space1 in ["Empty1"]:
            Space1 = "O"
    elif ComputerChoice in ["Empty2"]:
        if Space2 in ["X"]:
            pass
        elif Space2 in ["O"]:
            pass
        elif Space2 in ["Empty2"]:
            Space2 = "O"
    elif ComputerChoice in ["Empty3"]:
        if Space3 in ["X"]:
            pass
        elif Space3 in ["O"]:
            pass
        elif Space3 in ["Empty3"]:
            Space3 = "O"
    elif ComputerChoice in ["Empty4"]:
        if Space4 in ["X"]:
            pass
        elif Space4 in ["O"]:
            pass
        elif Space4 in ["Empty4"]:
            Space4 = "O"
    elif ComputerChoice in ["Empty5"]:
        if Space5 in ["X"]:
            pass
        elif Space5 in ["O"]:
            pass
        elif Space5 in ["Empty5"]:
            Space5 = "O"
    elif ComputerChoice in ["Empty6"]:
        if Space6 in ["X"]:
            pass
        elif Space6 in ["O"]:
            pass
        elif Space6 in ["Empty6"]:
            Space6 = "O"
    elif ComputerChoice in ["Empty7"]:
        if Space7 in ["X"]:
            pass
        elif Space7 in ["O"]:
            pass
        elif Space7 in ["Empty7"]:
            Space7 = "O"
    elif ComputerChoice in ["Empty8"]:
        if Space8 in ["X"]:
            pass
        elif Space8 in ["O"]:
            pass
        elif Space8 in ["Empty8"]:
            Space8 = "O"
    elif ComputerChoice in ["Empty9"]:
        if Space9 in ["X"]:
            pass
        elif Space9 in ["O"]:
            pass
        elif Space9 in ["Empty9"]:
            Space9 = "O"

    for x in TicBoard:
        TicBoard1 = [Space1, Space2, Space3]
        TicBoard2 = [Space4, Space5, Space6]
        TicBoard3 = [Space7, Space8, Space9]

        TicBoard = [TicBoard1, 
                    TicBoard2,
                    TicBoard3]
        print(x)

    print("The computer has gone now its your turn.")

    ChoiceOfSpace = str(input("Please choose a space to put an x in (Type numbers 1-9): "))

    if ChoiceOfSpace in ["1"]:
        if Space1 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space1 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space1 in ["Empty1"]:
            Space1 = "X"
            print("You have put an X in spot one!")
    elif ChoiceOfSpace in ["2"]:
        if Space2 not in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space2 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space2 in ["Empty2"]:
            Space2 = "X"
            print("You have put an X in spot two!")
    elif ChoiceOfSpace in ["3"]:
        if Space3 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space3 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space3 in ["Empty3"]:
            Space3 = "X"
            print("You have put an X in spot three!")
    elif ChoiceOfSpace in ["4"]:
        if Space4 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space4 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space4 in ["Empty4"]:
            Space4 = "X"
            print("You have put an X in spot four!")
    elif ChoiceOfSpace in ["5"]:
        if Space5 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space5 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space5 in ["Empty5"]:
            Space5 = "X"
            print("You have put an X in spot five!")
    elif ChoiceOfSpace in ["6"]:
        if Space6 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space6 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space6 in ["Empty6"]:
            Space6 = "X"
            print("You have put an X in spot six!")
    elif ChoiceOfSpace in ["7"]:
        if Space7 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space7 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space7 in ["Empty7"]:
            Space7 = "X"
            print("You have put an X in spot seven!")
    elif ChoiceOfSpace in ["8"]:
        if Space8 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space8 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space8 in ["Empty8"]:
            Space8 = "X"
            print("You have put an X in spot eight!")
    elif ChoiceOfSpace in ["9"]:
        if Space9 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space9 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space9 in ["Empty9"]:
            Space9 = "X"
            print("You have put an X in spot nine!")

    if Space1 in ["O"]:
        if Space2 in ["0"]:
            if Space3 in ["O"]:
                SomeoneHasWon = True
                print("The computer has won!")
        elif Space5 in ["O"]:
            if Space9 in ["O"]:
                SomeoneHasWon = True
                print("The computer has won!")
        elif Space4 in ["O"]:
            if Space7 in ["O"]:
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
        TicBoard1 = [Space1, Space2, Space3]
        TicBoard2 = [Space4, Space5, Space6]
        TicBoard3 = [Space7, Space8, Space9]

        TicBoard = [TicBoard1, 
                    TicBoard2,
                    TicBoard3]
        print(x)