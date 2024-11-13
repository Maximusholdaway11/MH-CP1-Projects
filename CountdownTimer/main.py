#Max Holdaway Countdown Timer

print("This is a simple timer.")

import time as time

time.sleep(2)

print("")

print("Loading")

time.sleep(2)

print("Loading")

time.sleep(2)

print("Loading")

time.sleep(2)

print("Loading")

time.sleep(4)

print("Finished")

print("")

TimerAmount = int(input("Please give me how many seconds you want the timer to last for: "))

while TimerAmount != 0:
    print(TimerAmount)
    TimerAmount -= 1
    time.sleep(1)
else:
    print(0)
    time.sleep(0.3)
    print("Timer has ended.")