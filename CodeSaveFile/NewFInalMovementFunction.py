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
    return GameMapFVar[CurrentPlayerSpaceFVar2[0]][CurrentPlayerSpaceFVar2[1]]

def PlayerCanMoveInSpace(CurrentPlayerSpaceFVar, GameMapFVar):
    if (
        (CurrentPlayerSpaceFVar[0] not in [0,1,2,3,4]) or
        (CurrentPlayerSpaceFVar[1] not in [0,1,2,3,4]) or
        GetMapSpace(CurrentPlayerSpaceFVar, GameMapFVar).startswith('Wall') 
    ):
        return False
    return True

def Movement(PlayerMovementDirectionFVar, CurrentPlayerSpaceFVar, GameMapFVar):
    PlayerMapSpace = [-1,-1]
    if PlayerMovementDirectionFVar.lower() == "left":
        PlayerMapSpace = [CurrentPlayerSpaceFVar[0], CurrentPlayerSpaceFVar[1] - 1]
    elif PlayerMovementDirectionFVar.lower() == "right":
        PlayerMapSpace = [CurrentPlayerSpaceFVar[0], CurrentPlayerSpaceFVar[1] + 1]
    elif PlayerMovementDirectionFVar.lower() == "up":
        PlayerMapSpace = [CurrentPlayerSpaceFVar[0] - 1, CurrentPlayerSpaceFVar[1]]
    elif PlayerMovementDirectionFVar.lower() == "down":
        PlayerMapSpace = [CurrentPlayerSpaceFVar[0] + 1, CurrentPlayerSpaceFVar[1]]
    if PlayerCanMoveInSpace(PlayerMapSpace, GameMapFVar):
        return PlayerMapSpace
    else:
        print(f"The move '{PlayerMoveDirection}' is not valid. Try a new movement.")
        return CurrentPlayerSpaceFVar
        

CurrentPlayerSpace = [0, 0]

GameMapRow1 = [Space1, Space2, Space3, Space4, Space5]
GameMapRow2 = [Space6, Space7, Space8, Space9, Space10]
GameMapRow3 = [Space11, Space12, Space13, Space14, Space15]
GameMapRow4 = [Space16, Space17, Space18, Space19, Space20]
GameMapRow5 = [Space21, Space22, Space23, Space24, Space25]
GameMap = [GameMapRow1, GameMapRow2, GameMapRow3, GameMapRow4, GameMapRow5]
print(GameMap)
PlayerMoveDirection = str(input("Which direction do you want to move?: "))

CurrentPlayerSpace = Movement(PlayerMoveDirection, CurrentPlayerSpace, GameMap)
print(CurrentPlayerSpace)
