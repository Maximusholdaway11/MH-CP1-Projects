#Max Holdaway Anagram Creator

import random

print("This is an Anagram Creator.")

print("")

EmptyStringVar = ""

OriginalMessage = str(input("Please give me a word to make anagrams from: "))

EmptyListVar = []

def AnagramMaker(NewMessage):
    NewMessage = list(NewMessage)
    random.shuffle(NewMessage)
    NewMessage = "".join(NewMessage)
    return NewMessage

print("")

x = 0

ListOfAnagrams = []

while x < 10:
    x = x + 1
    TempAppendVar = (AnagramMaker(OriginalMessage))
    ListOfAnagrams.append(TempAppendVar)

print(ListOfAnagrams)