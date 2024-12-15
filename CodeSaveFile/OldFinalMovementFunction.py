def Movement(SpacePlayerIsMovingTo, CurrentPlayerSpace):
    if CurrentPlayerSpace == "Exit/Start":
        if SpacePlayerIsMovingTo == "Enemy1":
            CurrentPlayerSpace = "Enemy1"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space6":
            CurrentPlayerSpace = "Space6"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Enemy1":
        if SpacePlayerIsMovingTo == "Exit/Start":
            CurrentPlayerSpace = "Exit/Start"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space6":
            CurrentPlayerSpace = "Space6"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space3":
            CurrentPlayerSpace = "Space3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space8":
            CurrentPlayerSpace = "Space8"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space3":
        if SpacePlayerIsMovingTo == "Enemy1":
            CurrentPlayerSpace = "Enemy1"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space4":
            CurrentPlayerSpace = "Space4"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space8":
            CurrentPlayerSpace = "Space8"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space4":
        if SpacePlayerIsMovingTo == "Space3":
            CurrentPlayerSpace = "Space3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest4":
            CurrentPlayerSpace = "Chest4"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space8":
            CurrentPlayerSpace = "Space8"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space10":
            CurrentPlayerSpace = "Space10"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Chest4":
        if SpacePlayerIsMovingTo == "Space10":
            CurrentPlayerSpace = "Space10"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space11":
            CurrentPlayerSpace = "Space11"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space6":
        if SpacePlayerIsMovingTo == "Exit/Start":
            CurrentPlayerSpace = "Exit/Start"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy1":
            CurrentPlayerSpace = "Enemy1"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space11":
            CurrentPlayerSpace = "Space11"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space8":
        if SpacePlayerIsMovingTo == "Space4":
            CurrentPlayerSpace = "Space4"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space3":
            CurrentPlayerSpace = "Space3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy1":
            CurrentPlayerSpace = "Enemy1"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest5":
            CurrentPlayerSpace = "Chest5"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space10":
        if SpacePlayerIsMovingTo == "Chest4":
            CurrentPlayerSpace = "Chest4"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest3":
            CurrentPlayerSpace = "Chest3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space4":
            CurrentPlayerSpace = "Space4"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space11":
        if SpacePlayerIsMovingTo == "Space6":
            CurrentPlayerSpace = "Space6"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space16":
            CurrentPlayerSpace = "Space16"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Chest5":
        if SpacePlayerIsMovingTo == "Space8":
            CurrentPlayerSpace = "Space8"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space18":
            CurrentPlayerSpace = "Space18"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Chest3":
        if SpacePlayerIsMovingTo == "Space10":
            CurrentPlayerSpace = "Space10"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space20":
            CurrentPlayerSpace = "Space20"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space16":
        if SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall5":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space11":
            CurrentPlayerSpace = "Space11"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest1":
            CurrentPlayerSpace = "Chest1"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Enemy2":
        if SpacePlayerIsMovingTo == "Chest5":
            CurrentPlayerSpace = "Chest5"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall5":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space11":
            CurrentPlayerSpace = "Space11"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest2":
            CurrentPlayerSpace = "Chest2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space18":
            CurrentPlayerSpace = "Space18"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space16":
            CurrentPlayerSpace = "Space16"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest1":
            CurrentPlayerSpace = "Chest1"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space18":
        if SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest5":
            CurrentPlayerSpace = "Chest5"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall3":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest2":
            CurrentPlayerSpace = "Chest2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall5":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Enemy3":
        if SpacePlayerIsMovingTo == "Space18":
            CurrentPlayerSpace = "Space18"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall3":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "FinalBoss":
            CurrentPlayerSpace = "FinalBoss"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest2":
            CurrentPlayerSpace = "Chest2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest5":
            CurrentPlayerSpace = "Chest5"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space20":
            CurrentPlayerSpace = "Space20"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space20":
        if SpacePlayerIsMovingTo == "FinalBoss":
            CurrentPlayerSpace = "FinalBoss"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall3":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest3":
            CurrentPlayerSpace = "Chest3"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Chest1":
        if SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space16":
            CurrentPlayerSpace = "Space16"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall5":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Chest2":
        if SpacePlayerIsMovingTo == "Space18":
            CurrentPlayerSpace = "Space18"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall5":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall3":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "FinalBoss":
        if SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space20":
            CurrentPlayerSpace = "Space20"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall3":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        else:
            print("Unexpected Error try again.")
            return CurrentPlayerSpace
    else:
        print("Unexpected Error Has Occurred Please Try Again You have been sent to the starting place.")
        CurrentPlayerSpace = "Exit/Start"
        return CurrentPlayerSpace