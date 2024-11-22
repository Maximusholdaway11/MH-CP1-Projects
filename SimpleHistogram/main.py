#Max Holdaway Simple Histogram

print("This is a simple histogram.")

HistoList1 = []

HistoList2 = []

HistoList3 = []

HistoList4 = []

HistoList5 = []

NumberOfHisto1 = int(input("Please give the first number for the first row of the histogram: "))

NumberOfHisto2 = int(input("Please give the second number for the second row of the histogram: "))

NumberOfHisto3 = int(input("Please give the third number for the third row of the histogram: "))

NumberOfHisto4 = int(input("Please give the fourth number for the fourth row of the histogram: "))

NumberOfHisto5 = int(input("Please give the fifth number for the fifth row of the histogram: "))

for num in range(NumberOfHisto1):
    HistoList1.append("*")

for num in range(NumberOfHisto2):
    HistoList2.append("*")

for num in range(NumberOfHisto3):
    HistoList3.append("*")

for num in range(NumberOfHisto4):
    HistoList4.append("*")

for num in range(NumberOfHisto5):
    HistoList5.append("*")

print("1: ", *HistoList1, sep="")

print("2: ", *HistoList2, sep="")

print("3: ", *HistoList3, sep="")

print("4: ", *HistoList4, sep="")

print("5: ", *HistoList5, sep="")