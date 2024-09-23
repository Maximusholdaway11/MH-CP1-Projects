#Max Holdaway Pig Latin Converter

print("This is a pig latin converter it converts english to pig latin each input is a different word translated.")

print("")

EnglishWord1 = str(input("Please give me a word to translate into pig latin: "))

EnglishWord2 = str(input("Please give me a second word to translate into pig latin: "))

EnglishWord3 = str(input("Please give me a third word to translate into pig latin: "))

print("")

TypeOfWord1 = (input("Is the first word start with A, E, I, O, or U? if so say True if not say False (Use uppercase for true or false): "))

TypeOfWord2 = (input("Is the second word start with A, E, I, O, or U? if so say True if not say False (Use uppercase for true or false): "))

TypeOfWord3 = (input("Is the third word start with A, E, I, O, or U? if so say True if not say False (Use uppercase for true or false): "))

def PigConverter(EnglishWord, PigLatinWord, SplitEnglishLetter, SplitEnglishWord):
    SplitEnglishWord = EnglishWord[1:5]
    SplitEnglishLetter = EnglishWord[0:1]
    SplitEnglishLetter = SplitEnglishLetter + "ay"
    EnglishWord = SplitEnglishWord + SplitEnglishLetter
    PigLatinWord = EnglishWord
    return PigLatinWord

def PigConverterAEIOU(EnglishWord, PigLatinWord):
    EnglishWord = EnglishWord + "ay"
    PigLatinWord = EnglishWord
    return PigLatinWord

print("")

if TypeOfWord1 == "True":
    PigLatin1 = PigConverterAEIOU(EnglishWord1, "")
elif TypeOfWord1 == "False":
    PigLatin1 = PigConverter(EnglishWord1, "", "", "")

if TypeOfWord2 == "True":
    PigLatin2 = PigConverterAEIOU(EnglishWord2, "")
elif TypeOfWord2 == "False":
    PigLatin2 = PigConverter(EnglishWord2, "", "", "")

if TypeOfWord3 == "True":
    PigLatin3 = PigConverterAEIOU(EnglishWord3, "")
elif TypeOfWord3 == "False":
    PigLatin3 = PigConverter(EnglishWord3, "", "", "")

print(PigLatin1, PigLatin2, PigLatin3)