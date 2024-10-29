#Max Holdaway What is my grade?

print("This is a grade calculator.")

NumberConstant = 0

ClassGradeList = []

def LetterGrader(NumberGrade):
    if NumberGrade >= 97:
        return "A+"
    elif NumberGrade <= 96.99 and NumberGrade >= 93:
        return "A"
    elif NumberGrade <= 92.99 and NumberGrade >= 90:
        return "A-"
    elif NumberGrade <= 89.99 and NumberGrade >= 87:
        return "B+"
    elif NumberGrade <= 86.99 and NumberGrade >= 83:
        return "B"
    elif NumberGrade <= 82.99 and NumberGrade >= 80:
        return "B-"
    elif NumberGrade <= 79.99 and NumberGrade >= 77:
        return "C+"
    elif NumberGrade <= 76.99 and NumberGrade >= 73:
        return "C"
    elif NumberGrade <= 72.99 and NumberGrade >= 70:
        return "C-"
    elif NumberGrade <= 69.99 and NumberGrade >= 67:
        return "D+"
    elif NumberGrade <= 66.99 and NumberGrade >= 65:
        return "D"
    elif NumberGrade <= 64.99 and NumberGrade >= 60:
        return "D-"
    elif NumberGrade <= 59.99:
        return "F"

while True:
    Choice = str(input(""""What do you want to do?
                       To check letter grades write Grades.
                       To exit write Exit\n"""))
    
    if Choice in ["Grades", "grades"]:
        while NumberConstant <= 6:
            NumberConstant += 1
            Class = ""
            Class = str(input("Please give me the class you want to use for checking grades: "))
            ClassGradeList.append(Class)
            Grade = ""
            Grade = float(input("Please give me the grade for the class: "))
            ClassGradeList.append(LetterGrader(Grade))
            print("")
        print("Here is a list of your classes and grades assoiated with them.")
        print(ClassGradeList)

    elif Choice in ["Exit", "exit"]:
        print("Thank you for using our grade calculator see you later!")
        break

    else:
        print("Unexpected Error try again")