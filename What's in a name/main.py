#Max Holdaway What's in a name raid

#Calculation for the area of a rectangle (squares as well because sqaures are another type of rectangle)
def AreaCalc(x, y):
    z = x * y
    return z

#Calculation for the volume of a rectangular prism (Cubes as well because cubes are another type of rectangular prism)
def VolumeCalc(a, b, c):
    area = AreaCalc(a, b)
    result = area * c
    return result

#Length and Width for the rectangle (squares as well because sqaures are another type of rectangle)
length = 5
width = 3
#Calculating the area for the rectangle (squares as well because sqaures are another type of rectangle)
Rectangle = AreaCalc(length, width)
print(f"The Rectangle's and or Sqaure's size is: {Rectangle}")

#Length, Width, and Height for the rectangular prism (Cubes as well because cubes are another type of rectangular prism)
length3d = 4
width3d = 6
height = 2
#Calcualting the volume for the rectangular prism (Cubes as well because cubes are another type of rectangular prism)
RectangularPrism = VolumeCalc(length3d, width3d, height)
print(f"The Rectangular Prism's and or Cube's size is: {RectangularPrism}")