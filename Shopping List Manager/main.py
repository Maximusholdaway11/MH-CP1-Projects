#Max Holdaway Shopping List Manager

EmptyShoppingList = []

while True:
    action = input("""what would you like to use?
                   Enter Add to add an item
                   Enter Remove to remove the items you type in (Please type it in as it is listed or it will break)
                   Enter Current Items to check what items you have in the list currently
                   Enter Exit to exit the shopping list manager\n""")
    
    if action in ["Add", "add"]:
        ChoiceOfAddition = input("What would you like to add to your shopping list?: ")
        EmptyShoppingList.append(ChoiceOfAddition)
        print("Your item was added succesfully!")
        print("")

    elif action in ["Current Items", "current items", "Current items", "current Items"]:
        print(f"Here is your shopping list {EmptyShoppingList}")
        print("")

    elif action in ["Remove", "remove"]:
        ChoiceOfRemoval = input("What would you like to remove from your shopping list?: ")
        EmptyShoppingList.remove(ChoiceOfRemoval)
        print("Succesfully removed the item from the list!")
        print("")

    elif action in ["Exit", "exit"]:
        print(f"Here is your shopping list {EmptyShoppingList} Exiting")
        break

    else:
        print("Unexpected Error please try again")