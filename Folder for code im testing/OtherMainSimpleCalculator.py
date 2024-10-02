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
                   Type Quotient for quotient divison\n""")
    if action in [Addition]:
        AdditionTerm1 = input("Please give me the first number to add: ")
        AdditionTerm2 = input("Please give me the second number to add: ")
        print(f"This is the sum {Addition(AdditionTerm1, AdditionTerm2)}")