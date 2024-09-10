#Max Holdaway Variables Infographic Ex Code

#Message to show what program does
print("this is a three term multiplacation only calculator (excluding variables like x and y)")

#Making space between the message and the input
print("")

#Asking to input first term in equation
FTerm = int(input("Please type the first term: "))

#Asking to input second term in euqation
STerm = int(input("Please type the second term: "))

#Asking to input third term in equation
ThTerm = int(input("Please type the third term: "))

#Using the three terms and multiplying them
SimTerm = FTerm*STerm*ThTerm

#Showing the user the result
print(f"Your answer is: {SimTerm}")