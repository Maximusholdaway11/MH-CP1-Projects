#Max Holdaway Shift Cipher

print("This is a shift cipher it encrypts messages for you.")

print("")

UnCryptedMessage = input("Please give me a message to encrypt: ")

ShiftingNumber = int(input("Please give me the number of times you want to shift your message for encrypting: "))

print("")

MessageList = []

def ShiftCrypting(Message, UnCryptedMessageVar):
    for character in Message:
        x = ord(character)
        x = x + ShiftingNumber
        UnCryptedMessageVar.append(chr(x))
    return UnCryptedMessageVar

