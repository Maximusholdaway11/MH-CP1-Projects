#Max Holdaway Shift Cipher

print("This is a shift cipher it encrypts messages for you.")

print("")

UnCryptedMessage = input("Please give me a message to encrypt: ")

CryptedMessage = input("Please give me a message to unencrypt: ")

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

def UnShiftCrypting(CryptedMessageVar, ShiftingVariable, x, EmptyList):
    for character in CryptedMessageVar:
        x = ord(character)
        x = x - ShiftingVariable
        EmptyList.append(chr(x))
        CryptedMessageVar = "".join(EmptyList)
    return CryptedMessageVar

print(f"This is the original UnCrypted message: {UnCryptedMessage}")

print("")

print(f"This is your Crypted message: {ShiftCrypting(UnCryptedMessage, ShiftingNumber, "", EmptyListVar)}")

print("")

print(f"This is your original Crypted message: {CryptedMessage}")

EmptyListVar = []

print("")

print(f"This is your UnCrypted message: {UnShiftCrypting(CryptedMessage, ShiftingNumber, "", EmptyListVar)}")