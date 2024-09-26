#Max Holdaway Anagram Creator

import random

print("This is an Anagram Creator.")

print("")

EmptyStringVar = ""

OriginalMessage = str(input("Please give me a word to make anagrams from: "))

OriginalMessage = OriginalMessage.split(EmptyStringVar)

print(OriginalMessage)

EmptyListVar = []

def AnagramMaker(NewMessage):
    random.shuffle(NewMessage)
    NewMessage = "".join(NewMessage)
    return NewMessage

print(AnagramMaker(OriginalMessage))