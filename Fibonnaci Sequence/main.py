#Max Holdaway Fibonnaci Sequence

print("This is a Fibonnaci Sequence Calculator. (If you start it with anything bigger than 1 it will break as well as it will also stop at 89)")

OneZeroisThere = False

ZeroVariable = 0

StartingValue = int(input("Please give me a starting value for the sequence: "))

print("")

while StartingValue < 89:
    if StartingValue == 0:
        print(StartingValue)
        StartingValue = StartingValue + 1
        OneZeroisThere = True
    elif StartingValue == 0 + 1:
        if OneZeroisThere == False:
            print(ZeroVariable)
        print(StartingValue)
        print(StartingValue)
        StartingValue = StartingValue + 1
    elif StartingValue == 1 + 1:
        print(StartingValue)
        StartingValue = StartingValue + 1
        print(StartingValue)
    elif StartingValue == 2 + 1:
        StartingValue = StartingValue + 2
        print(StartingValue)
    elif StartingValue == 3 + 2:
        StartingValue = StartingValue + 3
        print(StartingValue)
    elif StartingValue == 5 + 3:
        StartingValue = StartingValue + 5
        print(StartingValue)
    elif StartingValue == 8 + 5:
        StartingValue = StartingValue + 8
        print(StartingValue)
    elif StartingValue == 13 + 8:
        StartingValue = StartingValue + 13
        print(StartingValue)
    elif StartingValue == 21 + 13:
        StartingValue = StartingValue + 21
        print(StartingValue)
    elif StartingValue == 34 + 21:
        StartingValue = StartingValue + 34
        print(StartingValue)