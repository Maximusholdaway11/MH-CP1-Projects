#Max Holdaway Shift Cipher

print("This is a shift cipher it encrypts messages for you.")

print("")

UnCryptedMessage = input("Please give me a message to encrypt: ")

print("")

a = "a"

b = "b"

c = "c"

d = "d"

e = "e"

f = "f"

def ShiftCrypting(Message, CryptedMessage, SemiCryptedMessage, CharList):
    CharList = (a.ord, b.ord, c.ord, d.ord, e.ord, f.ord)
    CryptedMessage = CharList

print(ShiftCrypting(UnCryptedMessage, "", ""))