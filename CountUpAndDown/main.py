#Max Holdaway Counting Up and Down

print("This counts up to 20 and back down to zero.")

CountingNumber = 0

for num in range(21):
    print(CountingNumber)
    CountingNumber += 1
else:
    if CountingNumber == 21:
        print("Counting down now!")
        for num in range(21):
            CountingNumber -= 1
            print(CountingNumber)
            