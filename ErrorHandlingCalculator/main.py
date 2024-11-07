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
        AdditionTerm1 = input("Please give me the first number to add: ")
        AdditionTerm2 = input("Please give me the second number to add: ")
        try:
            float(AdditionTerm1)
            float(AdditionTerm2)
        except:
            print("You have not selected numbers.")
            continue
        else:
            AdditionTerm1 = float(AdditionTerm1)
            AdditionTerm2 = float(AdditionTerm2)
            print(f"This is the sum {Addition(AdditionTerm1, AdditionTerm2)}")

    elif action in ["Subtraction", "subtraction"]:
        SubtractionTerm1 = input("Please give me the first number to be subtracted from: ")
        SubtractionTerm2 = input("Please give me the second number to subtract: ")
        try:
            float(SubtractionTerm1)
            float(SubtractionTerm2)
        except:
            print("You have not selected numbers.")
            continue
        else:
            SubtractionTerm1 = float(SubtractionTerm1)
            SubtractionTerm2 = float(SubtractionTerm2)
            print(f"This is the result of the subtraction {Subtraction(SubtractionTerm1, SubtractionTerm2)}")

    elif action in ["Multiplication", "multiplication"]:
        MultiplicationTerm1 = input("Please give me the first number to multiply: ")
        MultiplicationTerm2 = input("Please give me the second number to multiply: ")
        try:
            float(MultiplicationTerm1)
            float(MultiplicationTerm2)
        except:
            print("You have not selected numbers.")
            continue
        else:
            MultiplicationTerm1 = float(MultiplicationTerm1)
            MultiplicationTerm2 = float(MultiplicationTerm2)
            print(f"This is the product {Multiplication(MultiplicationTerm1, MultiplicationTerm2)}")

    elif action in ["Division", "division"]:
        DivisionTerm1 = input("Please give me the first number for division: ")
        DivisionTerm2 = input("Please give me the second number for division: ")
        if DivisionTerm2 in ["0", 0]:
            print("You can't divide by zero.")
        else:
            try:
                float(DivisionTerm1)
                float(DivisionTerm2)
            except:
                print("You have not selected numbers.")
                continue
            else:
                DivisionTerm1 = float(DivisionTerm1)
                DivisionTerm2 = float(DivisionTerm2)
                print(f"This is the divided product {Division(DivisionTerm1, DivisionTerm2)}")

    elif action in ["Exponent", "exponent"]:
        ExponentTerm1 = input("Please give me a number to use: ")
        ExponentTerm2 = input("Please give me the exponent for the number: ")
        try:
            float(ExponentTerm1)
            float(ExponentTerm2)
        except:
            print("You have not selected numbers.")
            continue
        else:
            ExponentTerm1 = float(ExponentTerm1)
            ExponentTerm2 = float(ExponentTerm2)
            print(f"This is your product {Exponents(ExponentTerm1, ExponentTerm2)}")

    elif action in ["Modular", "modular"]:
            ModularTerm1 = input("Please give me the first number for modular division: ")
            ModularTerm2 = input("Please give me the second number for modular division: ")
            if ModularTerm2 in ["0", 0]:
                print("You can't divide by zero.")
            else:
                try:
                    float(ModularTerm1)
                    float(ModularTerm2)
                except:
                    print("You have not selected numbers.")
                    continue
                else:
                    ModularTerm1 = float(ModularTerm1)
                    ModularTerm2 = float(ModularTerm2)
                    print(f"This is your modulo product {ModularDivision(ModularTerm1, ModularTerm2)}")

    elif action in ["Quotient", "quotient"]:
        QuotientTerm1 = input("Please give me the first number for quotient division: ")
        QuotientTerm2 = input("Please give me the second number for quotient division: ")
        if QuotientTerm2 in ["0", 0]:
            print("You can't divide by zero.")
        else:
            try:
                float(QuotientTerm1)
                float(QuotientTerm2)
            except:
                print("You have not selected numbers.")
                continue
            else:
                QuotientTerm1 = float(QuotientTerm1)
                QuotientTerm2 = float(QuotientTerm2)
                print(f"This is your quotient product {QuotientDivision(QuotientTerm1, QuotientTerm2)}")

    elif action in ["Exit", "exit"]:
        print("")
        print("Okay Exiting")
        break

    else:
        print("Unexpected Error please try again")