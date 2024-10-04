#Max Holdaway Average Grade

print("This is a program that gives you an average for your grades.")

print("")

Class1 = float(input("Please give me your grade from the first class: "))

Class2 = float(input("Please give me your grade from the second class: "))

Class3 = float(input("Please give me your grade from the third class: "))

Class4 = float(input("Please give me your grade from the fourth class: "))

Class5 = float(input("Please give me your grade from the fifth class: "))

Class6 = float(input("Please give me your grade from the sixth class: "))

Class7 = float(input("Please give me your grade from the seventh class: "))

GradeSum = Class1 + Class2 + Class3 + Class4 + Class5 + Class6 + Class7

GradeAverage = round(GradeSum / 7, 2)

print("")

print(f"Here is your average {GradeAverage}")