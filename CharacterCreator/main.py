#Max Holdaway Character Creator

print("This is a character creator.")

EmptyStringVar = ""

while True:
    action = str(input("""What do you want to do?
                       To create a character type Create
                       To look a the created characters stats type Character
                       To exit type Exit\n"""))
    
    CharacterList = []

    if action in ["Create", "create"]:
        NewCharacter = []
        CharacterName = str(input("Please type a name for your character: "))
        print("Human, Demon, Aquatic, Dwarf")
        ChosenRace = str(input("Choose a race out of the options (please use capitals): "))
        print("Wizard, Knight, Archer, Healer")
        ChosenClass = str(input("Choose a class out of the options (please use capitals): "))
        print(f"Your new character {CharacterName} has been created!")
    
    elif action in ["Character", "character"]:
        print(f"Here is {CharacterName}'s stats")

        if ChosenRace in ["Human"]:
                Health = 15
                Strength = 15
                Dexterity = 15
                Intelligence = 15
        elif ChosenRace in ["Demon"]:
                Health = 12.5
                Strength = 15
                Dexterity = 12.5
                Intelligence = 20
        elif ChosenRace in ["Aquatic"]:
                Health = 15
                Strength = 12.5
                Dexterity = 17.5
                Intelligence = 15
        elif ChosenRace in ["Dwarf"]:
                Health = 20
                Strength = 20
                Dexterity = 20
                Intelligence = 10

        if ChosenClass in ["Wizard"]:
                Health -= 5
                Strength -= 5
                Dexterity -= 5
                Intelligence += 15
        elif ChosenClass in ["Knight"]:
                Strength += 2.5
                Dexterity += 2.5
                Intelligence -= 5
        elif ChosenClass in ["Archer"]:
                Health -= 2.5
                Dexterity -= 2.5
                Intelligence += 5
        elif ChosenClass in ["Healer"]:
                Health -= 7.5
                Strength -= 7.5
                Dexterity += 7.5
                Intelligence += 7.5
            
        print(f"This is your characters health: {Health}")
        print(f"This is your characters strength: {Strength}")
        print(f"This is your characters dexterity: {Dexterity}")
        print(f"This is your characters intelligence: {Intelligence}")
    
    elif action in ["Exit", "exit"]:
        print("Thanks for using our character creator come back soon!")
        break

    else:
        print("Unexpected Error try Again")
        continue

    