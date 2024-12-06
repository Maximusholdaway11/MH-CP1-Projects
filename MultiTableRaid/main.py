print("This is a full multiplication table generator.")

def Multiplication(x, y):
    z = x * y
    return z

Row1 = []

Row2 = []

Row3 = []

Row4 = []

Row5 = []

Row6 = []

Row7 = []

Row8 = []

Row9 = []

Row10 = []

Row11 = []

Row12 = []

OneRow = 1

TwoRow = 2

ThreeRow = 3

FourRow = 4

FiveRow = 5

SixRow = 6

SevenRow = 7

EightRow = 8

NineRow = 9

TenRow = 10

ElevenRow = 11

TwelveRow = 12

NumberConstant = 0

NumberConstant2 = 0

NumberConstant3 = 0

NumberConstant4 = 0

NumberConstant5 = 0

NumberConstant6 = 0

NumberConstant7 = 0

NumberConstant8 = 0

NumberConstant9 = 0

NumberConstant10 = 0

NumberConstant11 = 0

NumberConstant12 = 0

print("Here is your table")

for x in range(12):
    NumberConstant += 1
    Row1.append(Multiplication(OneRow, NumberConstant))

for x in range(12):
    NumberConstant2 += 1
    Row2.append(Multiplication(TwoRow, NumberConstant2))

for x in range(12):
    NumberConstant3 += 1
    Row3.append(Multiplication(ThreeRow, NumberConstant3))

for x in range(12):
    NumberConstant4 += 1
    Row4.append(Multiplication(FourRow, NumberConstant4))

for x in range(12):
    NumberConstant5 += 1
    Row5.append(Multiplication(FiveRow, NumberConstant5))

for x in range(12):
    NumberConstant6 += 1
    Row6.append(Multiplication(SixRow, NumberConstant6))

for x in range(12):
    NumberConstant7 += 1
    Row7.append(Multiplication(SevenRow, NumberConstant7))

for x in range(12):
    NumberConstant8 += 1
    Row8.append(Multiplication(EightRow, NumberConstant8))

for x in range(12):
    NumberConstant9 += 1
    Row9.append(Multiplication(NineRow, NumberConstant9))

for x in range(12):
    NumberConstant10 += 1
    Row10.append(Multiplication(TenRow, NumberConstant10))

for x in range(12):
    NumberConstant11 += 1
    Row11.append(Multiplication(ElevenRow, NumberConstant11))

for x in range(12):
    NumberConstant12 += 1
    Row12.append(Multiplication(TwelveRow, NumberConstant12))

Row1 = str(Row1)

StringRow1 = ''.join(Row1)

print(type(StringRow1))

print("{: >3}".format(StringRow1))
print(Row2)
print(Row3)