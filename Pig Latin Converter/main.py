#Max Holdaway Pig Latin Converter

print("This is a pig latin converter it converts english to pig latin each input is a different word translated.")

print("")

EnglishWord = str(input("Please give me a word to translate into pig latin: "))

EnglishWord2 = str(input("Please give me a second word to translate into pig latin: "))

def PigConverter(EnglishWord, PigLatinWord, SplitEnglishLetter, SplitEnglishWord):
    SplitEnglishWord = EnglishWord[1:5]
    SplitEnglishLetter = EnglishWord[0:1]
    SplitEnglishLetter = SplitEnglishLetter + "ay"
    EnglishWord = SplitEnglishWord + "-" + SplitEnglishLetter
    PigLatinWord = EnglishWord
    return PigLatinWord

print(PigConverter(EnglishWord, "", "", ""), PigConverter(EnglishWord2, "", "", ""))