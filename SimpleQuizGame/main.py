#Max Holdaway Simple Quiz Game

print("This is a simple quiz game with the topic being math.")

TotalScore = 0

Difficulty = ""

StartingQuestion = input("""What is 120 * 50
                     A. 6000
                     B. 3000
                     C. 9000
                     D. 12000
                     Type Your Answer Here: """)

if StartingQuestion in ["A"]:
    TotalScore += 1
    print("You got it correct!")
    Difficulty = "Normal"

    if Difficulty in ["Normal"]:
        Question2 = input("""What is 6 squared plus 4 squared
                              A. 50
                              B. 48
                              C. 52
                              D. 54
                              Type Your Answer Here: """)
        if Question2 in ["C"]:
            print("You got it correct!")
            TotalScore += 1
            Difficulty = "Normal"

            if Difficulty in ["Normal"]:
                Question6 = str(input("""What is the square root of 12544
                                      A. 147
                                      B. 135
                                      C. 112
                                      D. 122
                                      Type Your Answer Here: """))
                
                if Question6 in ["C"]:
                    print("You got it correct!")
                    TotalScore += 1
                    Difficulty = "Normal"
        
        elif Question2 in ["A", "B", "D"]:
            print("Sadly you got it wrong but the next question will be easier!")
            Difficulty = "Slightly Easier"

            if Difficulty in ["Slightly Easier"]:
                Question3 = str(input("""What is 120 - 70
                              A. 70
                              B. 40
                              C. 60
                              D. 50
                              Type Your Answer Here: """))
                
                if Question3 in ["D"]:
                    print("You got it correct!")
                    TotalScore += 1
                    Difficulty = "Normal"
    else:
        print("Unexpected Error Try Again")

elif StartingQuestion in ["B", "C", "D"]:
    print("Sadly you got it wrong but the next question will be easier!")
    Difficulty = "Slightly Easier"

    if Difficulty in ["Slightly Easier"]:
        Question3 = str(input("""What is 120 - 70
                              A. 70
                              B. 40
                              C. 60
                              D. 50
                              Type Your Answer Here: """))
        if Question3 in ["D"]:
            print("You got it correct!")
            TotalScore += 1
            Difficulty = "Normal"

            if Difficulty in ["Normal"]:
                Question5 = str(input("""Solve for x, 2(5x + 5) = 50
                                      A. 4
                                      B. 5
                                      C. 6
                                      D. 3
                                      Type Your Answer Here: """))
        
        elif Question3 in ["A", "B", "C"]:
            print("Sadly you got it wrong but the next question will be easier!")
            Difficulty = "Way Easier"

            if Difficulty in ["Way Easier"]:
                Question4 = str(input("""What is 1 + 1?
                              A. 1
                              B. 2
                              C. 3
                              D. 4
                              Type Your Answer Here: """))
    else:
        print("Unexpected Error Try Again")

else:
    print("Unexpected Error Try Again")

#Question4 = str(input("""What is 1 + 1?
#                     A. 1
#                     B. 2
#                     C. 3
#                     D. 4
#                     Type Your Answer Here: """))
#
#if Question4 not in [""]:
#    if Question4 in ["A"]:
#        TotalScore += 1
#        print("Thats correct!")
#        Diffuculty = "Way Easier"
#    elif Question4 in ["B", "C", "D"]:
#        print("Sadly you got it wrong.")