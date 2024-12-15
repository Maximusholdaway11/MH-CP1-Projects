Space1 = "Exit/Start"

Space2 = "Enemy1"

Space3 = "Space3"

Space4 = "Space4"

Space5 = "Chest4"

Space6 = "Space6"

Space7 = "Wall4"

Space8 = "Space8"

Space9 = "Wall1"

Space10 = "Space10"

Space11 = "Space11"

Space12 = "Wall6"

Space13 = "Chest5"

Space14 = "Wall2"

Space15 = "Chest3"

Space16 = "Space16"

Space17 = "Enemy2"

Space18 = "Space18"

Space19 = "Enemy3"

Space20 = "Space20"

Space21 = "Chest1"

Space22 = "Wall5"

Space23 = "Chest2"

Space24 = "Wall3"

Space25 = "FinalBoss"

def GetMapSpace(CurrentPlayerSpaceFVar2, GameMapFVar):
    SpecificList = []
    MapSpaceFVar = ""
    for x in GameMapFVar:
        print(CurrentPlayerSpaceFVar2)
        SpecificList = x[CurrentPlayerSpaceFVar2[0]]
        for y in SpecificList:
            MapSpaceFVar = y[CurrentPlayerSpaceFVar2[1]]
    return MapSpaceFVar

def Movement(PlayerMovementDirectionFVar, CurrentPlayerSpaceFVar):
    if PlayerMovementDirectionFVar == "Left":
        if CurrentPlayerSpaceFVar == [1, 2]:
            print("You can't move to the left there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [2, 2]:
            print("You can't move to the left there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [4, 2]:
            print("You can't move to the left there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [1, 4]:
            print("You can't move to the left there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [2, 4]:
            print("You can't move to the left there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [4, 4]:
            print("You can't move to the left there's a wall right there.")
        else:
            if CurrentPlayerSpaceFVar[1] > 0:
                CurrentPlayerSpaceFVar[1] += 1
            elif CurrentPlayerSpaceFVar == 0:
                print("You can't move left anymore you reached the wall of the cave.")
    elif PlayerMovementDirectionFVar == "Right":
        if CurrentPlayerSpaceFVar == [1, 2]:
            print("You can't move to the right there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [2, 2]:
            print("You can't move to the right there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [4, 2]:
            print("You can't move to the right there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [1, 0]:
            print("You can't move to the right there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [2, 0]:
            print("You can't move to the right there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [4, 0]:
            print("You can't move to the right there's a wall right there.")
        else:
            if CurrentPlayerSpaceFVar[1] < 4:
                CurrentPlayerSpaceFVar[1] -= 1
            elif CurrentPlayerSpaceFVar == 4:
                print("You can't move right anymore you reached the wall of the cave.")
    elif PlayerMovementDirectionFVar == "Up":
        if CurrentPlayerSpaceFVar == [3, 1]:
            print("You can't move up there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [3, 3]:
            print("You can't move up there's a wall right there.")
        else:
            if CurrentPlayerSpaceFVar[0] > 0:
                CurrentPlayerSpaceFVar[0] -= 1
            elif CurrentPlayerSpaceFVar == 0:
                print("You can't move up anymore you reached the wall of the cave.")
    elif PlayerMovementDirectionFVar == "Down":
        if CurrentPlayerSpaceFVar == [3, 1]:
            print("You can't move down there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [3, 3]:
            print("You can't move down there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [0, 1]:
            print("You can't move down there's a wall right there.")
        elif CurrentPlayerSpaceFVar == [0, 3]:
            print("You can't move down there's a wall right there.")
        else:
            if CurrentPlayerSpaceFVar[0] < 4:
                CurrentPlayerSpaceFVar[0] += 1
            elif CurrentPlayerSpaceFVar == 4:
                print("You can't move down anymore you reached the wall of the cave.")

CurrentPlayerSpace = [0, 0]

PlayerMoveDirection = str(input("Which direction do you want to move?: "))

GameMapRow1 = [Space1, Space2, Space3, Space4, Space5]

GameMapRow2 = [Space6, Space7, Space8, Space9, Space10]

GameMapRow3 = [Space11, Space12, Space13, Space14, Space15]

GameMapRow4 = [Space16, Space17, Space18, Space19, Space20]

GameMapRow5 = [Space21, Space22, Space23, Space24, Space25]

GameMap = [GameMapRow1, GameMapRow2, GameMapRow3, GameMapRow4, GameMapRow5]

CurrentPlayerSpace = Movement(PlayerMoveDirection, CurrentPlayerSpace)

print(type(0))

MapSpace = GetMapSpace(CurrentPlayerSpace, GameMap)

print(MapSpace)