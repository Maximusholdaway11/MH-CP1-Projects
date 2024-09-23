#Max Holdaway Pig Latin Converter

print("This is a pig latin converter it translates one word of english to pig latin.")

print("")

EnglishWord = str(input("Please give me a word to translate into pig latin: "))

def PigTranslator(EnglishWord, PigLatinWord, SplitEnglishWord):
    SplitEnglishWord = EnglishWord[1:5]

    PigLatinWord = EnglishWord
    print(PigLatinWord)

PigLatin = ""

PigTranslator(EnglishWord, PigLatin)