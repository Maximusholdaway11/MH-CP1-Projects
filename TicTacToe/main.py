#Max Holdaway Tic Tac Toe Game

import time as time

import random as random

def TicTacToeWin(TicTacBoardEqual):

    IfTicTacBoardIsWinnable = True

    ListItem = TicTacBoardEqual[0]

    for item in TicTacBoardEqual:
            if ListItem != item:
                IfTicTacBoardIsWinnable = False
                break

    if IfTicTacBoardIsWinnable == True:
        TicTacBoardEqual = True
    else:
        TicTacBoardEqual = False

    return TicTacBoardEqual

def PlayerOrComputerWin(TicTacBoardPCWin):
    
    IfTicBoardEqual = True

    WhoWon = "Nobody"

    ListItemWin = TicTacBoardPCWin[0]

    if ListItemWin == "O":
        for item in TicTacBoardPCWin:
            if ListItemWin != item:
                IfTicBoardEqual = False
                break
            else:
                IfTicBoardEqual = True
                WhoWon = "Computer"
        
    elif ListItemWin == "X":
        for item in TicTacBoardPCWin:
            if ListItemWin != item:
                IfTicBoardEqual = False
                break
            else:
                IfTicBoardEqual = True
                WhoWon = "Player"
    else:
        WhoWon = "Nobody"

    return WhoWon

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

TicBoard1UpDown = [Space1, Space4, Space7]
TicBoard2UpDown = [Space2, Space5, Space8]
TicBoard3UpDown = [Space3, Space6, Space9]

TicBoardDiagonal1 = [Space1, Space5, Space9]
TicBoardDiagonal2 = [Space3, Space5, Space7]

TicBoard = [TicBoard1, 
            TicBoard2,
            TicBoard3]

SomeoneHasWon = False

while SomeoneHasWon == False:

    TicBoard1 = [Space1, Space2, Space3]
    TicBoard2 = [Space4, Space5, Space6]
    TicBoard3 = [Space7, Space8, Space9]

    TicBoard1UpDown = [Space1, Space4, Space7]
    TicBoard2UpDown = [Space2, Space5, Space8]
    TicBoard3UpDown = [Space3, Space6, Space9]

    TicBoardDiagonal1 = [Space1, Space5, Space9]
    TicBoardDiagonal2 = [Space3, Space5, Space7]

    TicBoard1Equal = TicTacToeWin(TicBoard1)

    TicBoard2Equal = TicTacToeWin(TicBoard2)

    TicBoard3Equal = TicTacToeWin(TicBoard3)

    TicBoardDiagonal1Equal = TicTacToeWin(TicBoardDiagonal1)

    TicBoardDiagonal2Equal = TicTacToeWin(TicBoardDiagonal2)

    TicBoard1UpDownEqual = TicTacToeWin(TicBoard1UpDown)

    TicBoard2UpDownEqual = TicTacToeWin(TicBoard2UpDown)

    TicBoard3UpDownEqual = TicTacToeWin(TicBoard3UpDown)

    TicBoard1PCwin = TicTacToeWin(TicBoard1)

    TicBoard2PCwin = TicTacToeWin(TicBoard2)

    TicBoard3PCwin = TicTacToeWin(TicBoard3)

    TicBoardDiagonal1PCwin = PlayerOrComputerWin(TicBoardDiagonal1)

    TicBoardDiagonal2PCwin = PlayerOrComputerWin(TicBoardDiagonal2)

    TicBoard1UpDownPCwin = PlayerOrComputerWin(TicBoard1UpDown)

    TicBoard2UpDownPCwin = PlayerOrComputerWin(TicBoard2UpDown)

    TicBoard3UpDownPCwin = PlayerOrComputerWin(TicBoard3UpDown)

    ComputerChoice = random.choice(["Empty1", "Empty2", "Empty3", "Empty4", "Empty5", "Empty6", "Empty7", "Empty8", "Empty9"])

    if ComputerChoice in ["Empty1"]:
        if Space1 in ["X"]:
            Space1 = Space1
        elif Space1 in ["O"]:
            Space1 = Space1
        elif Space1 in ["Empty1"]:
            Space1 = "O"
    elif ComputerChoice in ["Empty2"]:
        if Space2 in ["X"]:
            Space1 = Space1
        elif Space2 in ["O"]:
            Space1 = Space1
        elif Space2 in ["Empty2"]:
            Space2 = "O"
    elif ComputerChoice in ["Empty3"]:
        if Space3 in ["X"]:
            Space1 = Space1
        elif Space3 in ["O"]:
            Space1 = Space1
        elif Space3 in ["Empty3"]:
            Space3 = "O"
    elif ComputerChoice in ["Empty4"]:
        if Space4 in ["X"]:
            Space1 = Space1
        elif Space4 in ["O"]:
            pSpace1 = Space1
        elif Space4 in ["Empty4"]:
            Space4 = "O"
    elif ComputerChoice in ["Empty5"]:
        if Space5 in ["X"]:
            Space1 = Space1
        elif Space5 in ["O"]:
            Space1 = Space1
        elif Space5 in ["Empty5"]:
            Space5 = "O"
    elif ComputerChoice in ["Empty6"]:
        if Space6 in ["X"]:
            Space1 = Space1
        elif Space6 in ["O"]:
            Space1 = Space1
        elif Space6 in ["Empty6"]:
            Space6 = "O"
    elif ComputerChoice in ["Empty7"]:
        if Space7 in ["X"]:
            Space1 = Space1
        elif Space7 in ["O"]:
            Space1 = Space1
        elif Space7 in ["Empty7"]:
            Space7 = "O"
    elif ComputerChoice in ["Empty8"]:
        if Space8 in ["X"]:
            Space1 = Space1
        elif Space8 in ["O"]:
            Space1 = Space1
        elif Space8 in ["Empty8"]:
            Space8 = "O"
    elif ComputerChoice in ["Empty9"]:
        if Space9 in ["X"]:
            Space1 = Space1
        elif Space9 in ["O"]:
            Space1 = Space1
        elif Space9 in ["Empty9"]:
            Space9 = "O"

    print("")

    for x in TicBoard:
        TicBoard = [TicBoard1, 
                    TicBoard2,
                    TicBoard3]
        print(x)

    print("")

    print("The computer has gone now its your turn.")

    ChoiceOfSpace = str(input("Please choose a space to put an x in (Type numbers 1-9): "))

    if TicBoard1Equal == True and TicBoard1PCwin == "Computer":
        SomeoneHasWon = True
        print("The computer has won!")

    elif TicBoard2Equal == True and TicBoard2PCwin == "Computer":
        SomeoneHasWon = True
        print("The computer has won!")

    elif TicBoard3Equal == True and TicBoard3PCwin == "Computer":
        SomeoneHasWon = True
        print("The computer has won!")

    elif TicBoard1UpDownEqual == True and TicBoard1UpDownPCwin == "Computer":
        SomeoneHasWon = True
        print("The computer has won!")

    elif TicBoard2UpDownEqual == True and TicBoard2UpDownPCwin == "Computer":
        SomeoneHasWon = True
        print("The computer has won!")

    elif TicBoard3UpDownEqual == True and TicBoard3UpDownPCwin == "Computer":
        SomeoneHasWon = True
        print("The computer has won!")

    elif TicBoardDiagonal1Equal == True and TicBoardDiagonal1PCwin == "Computer":
        SomeoneHasWon = True
        print("The computer has won!")

    elif TicBoardDiagonal2Equal == True and TicBoardDiagonal2PCwin == "Computer":
        SomeoneHasWon = True
        print("The computer has won!")

    elif TicBoard1Equal == True and TicBoard1PCwin == "Player":
        SomeoneHasWon = True
        print("You have won!")

    elif TicBoard2Equal == True and TicBoard2PCwin == "Player":
        SomeoneHasWon = True
        print("You have won!")

    elif TicBoard3Equal == True and TicBoard3PCwin == "Player":
        SomeoneHasWon = True
        print("You have won!")

    elif TicBoard1UpDownEqual == True and TicBoard1UpDownPCwin == "Player":
        SomeoneHasWon = True
        print("You have won!")

    elif TicBoard2UpDownEqual == True and TicBoard2UpDownPCwin == "Player":
        SomeoneHasWon = True
        print("You have won!")

    elif TicBoard3UpDownEqual == True and TicBoard3UpDownPCwin == "Player":
        SomeoneHasWon = True
        print("You have won!")

    elif TicBoardDiagonal1Equal == True and TicBoardDiagonal1PCwin == "Player":
        SomeoneHasWon = True
        print("You have won!")

    elif TicBoardDiagonal2Equal == True and TicBoardDiagonal2PCwin == "Player":
        SomeoneHasWon = True
        print("You have won!")

    if ChoiceOfSpace in ["1"]:
        if Space1 in ["O"]:
            print("Sadly the computer has already taken this space try a different one.")
        elif Space1 in ["X"]:
            print("You already put something there! Please try again.")
        elif Space1 in ["Empty1"]:
            Space1 = "X"
            print("You have put an X in spot one!")
    elif ChoiceOfSpace in ["2"]:
        if Space2 in ["O"]:
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

    for x in TicBoard:
        TicBoard1 = [Space1, Space2, Space3]
        TicBoard2 = [Space4, Space5, Space6]
        TicBoard3 = [Space7, Space8, Space9]

        TicBoard = [TicBoard1, 
                    TicBoard2,
                    TicBoard3]
        print(x)