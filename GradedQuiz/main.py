#Max Holdaway Graded Quiz

#Making the total score variable
Total_Score = 0

#Starting message for quiz
print("This is a quiz on basic arithmetic math")

#Making a space bewteen starting message and questions
print("")

#First Question
Correct_Answer1 = int(input("What is 10 * 2?: "))

#Checking if the answer is right and telling user if it is right or wrong
if Correct_Answer1 == 20:
    print("You got it right! +1 to score")
    Total_Score = Total_Score + 1
else:
    print("You got it wrong no score added")

#Making a space between first and second question
print("")

#Second Question
Correct_Answer2 = float(input("What is 120 + 53.5?: "))

#Checking if the answer is right and telling user if it is right or wrong
if Correct_Answer2 == 173.5:
    print("You got it right! +1 to score")
    Total_Score = Total_Score + 1
else:
    print("You got it wrong no score added")

#Making a space between second and third question
print("")

#Third Question
Correct_Answer3 = int(input("What is 120 / 60?: "))

#Checking if the answer is right and telling user if it is right or wrong
if Correct_Answer3 == 20:
    print("You got it right! +1 to score")
    Total_Score = Total_Score + 1
else:
    print("You got it wrong no score added")

#Making a space between third and fourth question
print("")

#Fourth Question
Correct_Answer4 = float(input("What is 17.8 * 2?: "))

#Checking if the answer is right and telling user if it is right or wrong
if Correct_Answer4 == 35.6:
    print("You got it right! +1 to score")
    Total_Score = Total_Score + 1
else:
    print("You got it wrong no score added")

#Making a space between fourth and fifth question
print("")

#Fifth Question
Correct_Answer5 = int(input("What is 12345 + 6789?: "))

#Checking if the answer is right and telling user if it is right or wrong
if Correct_Answer5 == 19134:
    print("You got it right! +1 to score")
    Total_Score = Total_Score + 1
else:
    print("You got it wrong no score added")

#Making a space between the fifth question and the results
print("")

#Printing the results for the user
print(f"Here is your score {Total_Score} out of 5.")

