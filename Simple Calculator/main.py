#Max Holaway Simple calculator

#Explaining what the program does
print("This is an arithmetic only calculator with a few exceptions namely: Modulo, Exponents, and Rounded Division")

#Putting a space between the starting message and input messages
print("")

#Getting the numbers used for equations
NumberTerm1 = int(input("Type the first number to be used: "))

NumberTerm2 = int(input("Type the second number to be used: "))

#All the functions and variables used for the calculator
def Addition(x, y):
    z = x + y
    return z

Solution = Addition(NumberTerm1, NumberTerm2)

def Subtraction(x, y):
    z = x - y
    return z

MinusSolution = Subtraction(NumberTerm1, NumberTerm2)

def Multiplication(x, y):
    z = x * y
    return z

Product = Multiplication(NumberTerm1, NumberTerm2)

def Division(x, y):
    z = x / y
    return z

DividedProduct = Division(NumberTerm1, NumberTerm2)

def Exponents(x, y):
    z = x ** y
    return z

ExponentProduct = Exponents(NumberTerm1, NumberTerm2)

def ModularDivision(x, y,):
    z = x % y
    return z

ModularProduct = ModularDivision(NumberTerm1, NumberTerm2)

def QuotientDivision(x, y):
    z = x // y
    return z

QuotientProduct = QuotientDivision(NumberTerm1, NumberTerm2)

#Another space between messages
print("")

#Asking the user to tell the program which type of arithmetic they want to use and or which exception as well
Arithmetic = int(input("Tell me which type of arithmetic you want to calculate or which execption, Addition is 1, Subtraction is 2, and Multiplication is 3, Division is 4, Exponents is 5, Modular division is 6, and Quotient Division is 7: "))

#Another space between messages
print("")

#Deciding based on input which type of arithemtic or exception to print out
if Arithmetic == 1:
    print(f"{Solution}")
elif Arithmetic == 2:
    print(f"{MinusSolution}")
elif Arithmetic == 3:
    print(f"{Product}")
elif Arithmetic == 4:
    print(round(DividedProduct, 2))
elif Arithmetic == 5:
    print(f"{ExponentProduct}")
elif Arithmetic == 6:
    print(f"{ModularProduct}")
elif Arithmetic == 7:
    print(f"{QuotientProduct}")



