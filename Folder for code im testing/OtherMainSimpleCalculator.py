#Max Holdaway Improved Simple Calculator

#Explaining what the program does
print("This is an arithmetic only calculator with a few exceptions namely: Modulo, Exponents, and Rounded Division")

#Putting a space between the starting message and input messages
print("")

#All the functions and variables used for the calculator
def Addition(x, y):
    z = x + y
    return z

def Subtraction(x, y):
    z = x - y
    return z

def Multiplication(x, y):
    z = x * y
    return z

def Division(x, y):
    z = x / y
    return z

def Exponents(x, y):
    z = x ** y
    return z

def ModularDivision(x, y,):
    z = x % y
    return z

def QuotientDivision(x, y):
    z = x // y
    return z

while True:
    action = input("""what do you want to calculate?
                   Type Addition for addition
                   Type Subtraction for subtraction
                   Type Multiplication for multiplication
                   Type Division for division
                   Type Exponent for exponent
                   Type Modular for modular division
                   Type Quotient for quotient divison
                   Type Exit to exit the calculator\n""")
    
    if action in ["Addition", "addition"]:
        AdditionTerm1 = float(input("Please give me the first number to add: "))
        AdditionTerm2 = float(input("Please give me the second number to add: "))
        print(f"This is the sum {Addition(AdditionTerm1, AdditionTerm2)}")

    elif action in ["Subtraction", "subtraction"]:
        SubtractionTerm1 = float(input("Please give me the first number to be subtracted from: "))
        SubtractionTerm2 = float(input("Please give me the second number to subtract: "))
        print(f"This is the result of the subtraction {Subtraction(SubtractionTerm1, SubtractionTerm2)}")

    elif action in ["Multiplication", "multiplication"]:
        MultiplicationTerm1 = float(input("Please give me the first number for multiplication: "))
        MultiplicationTerm2 = float(input("Please give me the second number for multiplication: "))
        print(f"This is the product {Multiplication(MultiplicationTerm1, MultiplicationTerm2)}")

    elif action in ["Division", "division"]:
        DivisionTerm1 = float(input("Please give me the first number for division: "))
        DivisionTerm2 = float(input("Please give me the second number for division: "))
        print(f"This is the divided product {Division(DivisionTerm1, DivisionTerm2)}")

    elif action in ["Exponent", "exponent"]:
        ExponentTerm1 = float(input("Please give me a number to use: "))
        ExponentTerm2 = float(input("Please give me the exponent for the number: "))
        print(f"This is your product {Exponents(ExponentTerm1, ExponentTerm2)}")

    elif action in ["Exit", "exit"]:
        print("")
        print("Okay Exiting")
        break

    else:
        print("Unexpected Error please try again")