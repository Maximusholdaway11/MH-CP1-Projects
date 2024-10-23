#Max Holdaway List of Classes

print("This is a class lister.")

ClassList = ["Advisory", "Chemistry 1010", "CS 1400", "English 10 Honors", "Leadership 2 / ACT Prep", "Secondary Math 2 Honors", "Study Hall"]

#Don't Worry about the function I was just messing around with this to see if I could make something that takes in inputs to make a list
def ClassListMaker(ListVariable):
        ListVariable = []
        while len(ListVariable) <= 9:
            ListVariable.append((input("Please give a class to list: ")))
        return ListVariable

print(ClassList[0])

print(ClassList[1])

print(ClassList[2])

print(ClassList[3])

print(ClassList[4])

print(ClassList[5])

print(ClassList[6])