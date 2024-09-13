#Max Holaway Numbers profficency test

print("This is an arithmetic only calculator with a few exceptions namely: Modulo, Exponents, and Rounded Division")

NumberTerm1 = float(input("Type the first number to be used: "))

NumberTerm2 = float(input("Type the second number to be used: "))

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

Arithmetic = int(input("Tell me which type of arithmetic you want to calculate or which execption, Addition is 1, Subtraction is 2, and Multiplication is 3, Division is 4, : "))

if Arithmetic == 1:
    print(f"{Solution}")
elif Arithmetic == 2:
    print(f"{MinusSolution}")
elif Arithmetic == 3:
    print(f"{Product}")
elif Arithmetic == 4:
    print(f"{DividedProduct}")



