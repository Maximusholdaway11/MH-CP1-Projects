#Max Holdaway Fix the Bug Number 8

def is_between(num):
    if num >= 10 and num <= 20:
        return True
    return False

NumberInput = int(input("Please give me a number: "))

print(is_between(NumberInput))