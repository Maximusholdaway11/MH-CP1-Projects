#Max Holdaway Error Handling Calculator

print("This is an arithmetic only calculator with a few exceptions namely: Modulo, Exponents, and Rounded Division")

print("")

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

def ModularDivision(x, y):
    z = x % y
    return z

def QuotientDivision(x, y):
    z = x // y
    return z

while True:
    action = int(input("""what do you want to calculate?
                   Type Addition for addition
                   Type Subtraction for subtraction
                   Type Multiplication for multiplication
                   Type Division for division
                   Type Exponent for exponent
                   Type Modular for modular division
                   Type Quotient for quotient divison
                   Type Exit to exit the calculator\n"""))
    
    if action in ["Addition", "addition"]:
        try:
            AdditionTerm1 += 1
            AdditionTerm2 += 1
        except:
            print("You have not selected numbers.")
            continue
        else:
            AdditionTerm1 = float(input("Please give me the first number to add: "))
            AdditionTerm2 = float(input("Please give me the second number to add: "))
            print(f"This is the sum {Addition(AdditionTerm1, AdditionTerm2)}")

    elif action in ["Subtraction", "subtraction"]:
        try:
            SubtractionTerm1 += 1
            SubtractionTerm2 += 1
        except:
            print("You have not selected numbers.")
            continue
        else:
            SubtractionTerm1 = float(input("Please give me the first number to be subtracted from: "))
            SubtractionTerm2 = float(input("Please give me the second number to subtract: "))
            print(f"This is the result of the subtraction {Subtraction(SubtractionTerm1, SubtractionTerm2)}")

    elif action in ["Multiplication", "multiplication"]:
        try:
            MultiplicationTerm1 += 1
            MultiplicationTerm2 += 1
        except:
            print("You have not selected numbers.")
            continue
        else:
            MultiplicationTerm1 = float(input("Please give me the first number for multiplication: "))
            MultiplicationTerm2 = float(input("Please give me the second number for multiplication: "))
            print(f"This is the product {Multiplication(MultiplicationTerm1, MultiplicationTerm2)}")

    elif action in ["Division", "division"]:
        try:
            DivisionTerm1 += 1
            DivisionTerm2 += 1
        except:
            print("You have not selected numbers.")
            continue
        else:
            if DivisionTerm1 or DivisionTerm2 == 0:
                print("You cannot divide by 0 please try again.")
                continue
            else:
                DivisionTerm1 = float(input("Please give me the first number for division: "))
                DivisionTerm2 = float(input("Please give me the second number for division: "))
                print(f"This is the divided product {Division(DivisionTerm1, DivisionTerm2)}")

    elif action in ["Exponent", "exponent"]:
        try:
            ExponentTerm1 += 1
            ExponentTerm2 += 1
        except:
            print("You have not selected numbers.")
        else:
            ExponentTerm1 = float(input("Please give me a number to use: "))
            ExponentTerm2 = float(input("Please give me the exponent for the number: "))
            print(f"This is your product {Exponents(ExponentTerm1, ExponentTerm2)}")

    elif action in ["Modular", "modular"]:
        ModularTerm1 = float(input("Please give me the first number for modular division: "))
        ModularTerm2 = float(input("Please give me the second number for modular division: "))
        print(f"This is your modulo product {ModularDivision(ModularTerm1, ModularTerm2)}")

    elif action in ["Quotient", "quotient"]:
        QuotientTerm1 = float(input("Please give me the first number for quotient division: "))
        QuotientTerm2 = float(input("Please give me the second number for quotient division: "))
        print(f"This is your quotient product {QuotientDivision(QuotientTerm1, QuotientTerm2)}")

    elif action in ["Exit", "exit"]:
        print("")
        print("Okay Exiting")
        break

    else:
        print("Unexpected Error please try again")