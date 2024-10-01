#Max Holdaway Area Calculator

import math

print("This is an area calculator it calculates the area of a Square, Rectangle, Triangle, Circle, And Trapezoid.")

print("")

FirstLength = input("Please give me the Sidelength of Square / Rectangle Length / Triangle Base / Radius of circle / First Base of Trapezoid: ")

SecondLength = input("Please give me the Rectangle Width / Triangle Height / Second Base of Trapezoid (Even if your only calulating a sqaure): ")

ThirdLength = input("Please give me the height of Trapezoid (Even if your not using the trapezoid area calc or Calculating a sqaure): ")

pi = math.pi

def AreaOfSqaure(SideLength):
    A = SideLength ** 2
    return A

def AreaOfRectangle(Length, Width):
    A = Length * Width
    return A

def AreaOfTriangle(Base, Height):
    A = 0.5(Base * Height)
    return A

def AreaOfCircle(Radius):
    A = pi * (Radius ** 2)
    return A

def AreaOfTrapezoid(Base1, Base2, Height):
    A = ((Base1 + Base2)/2) * Height
    return A

print("")

TypeOfArea = input("Please tell me the type of area you want me to calculate: ")

print("")

if TypeOfArea in ["Sqaure", "square"]:
    print((f"This is the area of your sqaure {AreaOfSqaure(FirstLength)}"))

if TypeOfArea in ["Rectangle", "rectangle"]:
    print(f"This is the area of your rectangle {AreaOfRectangle(FirstLength, SecondLength)}")

if TypeOfArea in ["Triangle", "triangle"]:
    print((f"This is the area of your triangle {AreaOfTriangle(FirstLength, SecondLength)}"))

if TypeOfArea in ["Circle", "circle"]:
    print()