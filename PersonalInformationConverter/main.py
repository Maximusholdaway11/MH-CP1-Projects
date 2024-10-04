#Max Holdaway Personal Information Converter

print("This will convert information from strings that you input into the correct type of values as an output")

print("")

Name = input("Please give me your name: ")

Height = str(input("Please give me your height in meters: "))

Age = str(input("Please give me your age in years: "))

FavoriteNumber = str(input("Please give me your favorite number: "))

print("")

print(f"These are the original values or inputs of your name: {Name}, your height: {Height}, your age: {Age}, and your favorite number: {FavoriteNumber} as well as the types of the values type for your name: {type(Name)}, height: {type(Height)}, age: {type(Age)}, and favorite number: {type(FavoriteNumber)}")

Name = str(Name)

Height = float(Height)

Age = int(Age)

FavoriteNumber = int(FavoriteNumber)

print("")

print(f"These are the new changed values or inputs of your name: {Name}, your height: {Height}, your age: {Age}, and your favorite number: {FavoriteNumber} as well as the types of the values type for your name: {type(Name)}, height: {type(Height)}, age: {type(Age)}, and favorite number: {type(FavoriteNumber)}")