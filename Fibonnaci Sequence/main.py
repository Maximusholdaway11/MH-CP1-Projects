#Max Holdaway Fibonnaci Sequence

print("This is a Fibonnaci Sequence Calculator Please only start it with either 0 or 1. (If you start it with anything bigger than 1 it will partially break and when its bigger than 3 it will completely break as well as it will also stop at 89)")

print("")

ZeroVariable = 0

StartingValue = int(input("Please give me a starting value for the sequence: "))

print("")

while StartingValue < 89:
    if StartingValue == 0:
        StartingValue = StartingValue + 1
        FirstSequenceNumber = StartingValue
    elif StartingValue == 0 + 1:
        StartingValue = StartingValue + 1
        FirstSequenceNumber = 1
        SecondSequenceNumber = StartingValue
    elif StartingValue == 1 + 1:
        StartingValue = StartingValue + 1
        ThirdSequenceNumber = StartingValue
    elif StartingValue == 2 + 1:
        StartingValue = StartingValue + 2
        FourthSequenceNumber = StartingValue
    elif StartingValue == 3 + 2:
        StartingValue = StartingValue + 3
        FifthSequenceNumber = StartingValue
    elif StartingValue == 5 + 3:
        StartingValue = StartingValue + 5
        SixthSequenceNumber = StartingValue
    elif StartingValue == 8 + 5:
        StartingValue = StartingValue + 8
        SeventhSequenceNumber = StartingValue
    elif StartingValue == 13 + 8:
        StartingValue = StartingValue + 13
        EighthSequenceNumber = StartingValue
    elif StartingValue == 21 + 13:
        StartingValue = StartingValue + 21
        NinthSequenceNumber = StartingValue
    elif StartingValue == 34 + 21:
        StartingValue = StartingValue + 34
        TenthSequenceNumber = StartingValue

FibonacciList = list[ZeroVariable, FirstSequenceNumber, FirstSequenceNumber, SecondSequenceNumber, ThirdSequenceNumber, FourthSequenceNumber, FifthSequenceNumber, SixthSequenceNumber, SeventhSequenceNumber, EighthSequenceNumber, NinthSequenceNumber, TenthSequenceNumber]

print("This is the Fibonacci Sequence", FibonacciList)