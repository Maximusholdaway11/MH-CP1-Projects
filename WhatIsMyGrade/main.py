#Max Holdaway What is my grade?

print("This is a grade calculator.")

NumberConstant = 0

ClassGradeList = []

def LetterGrader(NumberGrade):
    if NumberGrade >= 93:
        return "A"

while True:
    Choice = str(input(""""What do you want to do?
                       To check letter grades write Grades.
                       To exit write Exit\n"""))
    
    if Choice in ["Grades", "grades"]:
        while NumberConstant <= 7:
            NumberConstant += 1
            Class = ""
            Class = str(input("Please give me the class you want to use for checking grades: "))
            ClassGradeList.append(Class)
            Grade = ""
            Grade = float(input("Please give me the grade for the class: "))
            ClassGradeList.append(Grade)
            print("")
        print(ClassGradeList)

    elif Choice in ["Exit", "exit"]:
        print("Thank you for using our grade calculator see you later!")
        break

    else:
        print("Unexpected Error try again")
