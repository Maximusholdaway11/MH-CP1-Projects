#Max Holdaway Simple Quiz Game

print("This is a simple quiz game with the topic being math.")

TotalScore = 0

Difficulty = ""

StartingQuestion = int(input("""What is 120 * 50
                     A. 6000
                     B. 3000
                     C. 9000
                     D. 12000
                     Type Your Answer Here: """))

if StartingQuestion == 6000:
    TotalScore += 1
    print("You got it correct!")
    Difficulty = "Normal"
    if Difficulty in ["Normal"]:
        Question2 = int(input("""What is 6 squared plus 4 squared
                              A. 50
                              B. 48
                              C. 52
                              D. 54
                              Type Your Answer Here: """))
elif StartingQuestion in [3000, 9000, 12000]:
    print("Sadly you got it wrong but the next question will be easier!.")
    Difficulty = "Slightly Easier"
    if Difficulty in ["Slightly Easier"]:
        print("Code Works")
        Question3 = int(input("""What is 120 - 70
                              A. 70
                              B. 40
                              C. 60
                              D. 50
                              Type Your Answer Here: """))

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