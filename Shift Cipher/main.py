#Max Holdaway Shift Cipher

print("This is a shift cipher it encrypts messages for you.")

print("")

UnCryptedMessage = input("Please give me a message to encrypt: ")

ShiftingNumber = int(input("Please give me the number of times you want to shift your message for encrypting: "))

print("")

EmptyListVar = []

def ShiftCrypting(UnCryptedMessageVar, ShiftingVariable, x, EmptyList):
    for character in UnCryptedMessageVar:
        x = ord(character)
        x = x + ShiftingVariable
        EmptyList.append(chr(x))
        UnCryptedMessageVar = "".join(EmptyList)
    return UnCryptedMessageVar

print(ShiftCrypting(UnCryptedMessage, ShiftingNumber, "", EmptyListVar))