#Max Holdaway Final Project

import random as random

print("This is my adventure game, have a good time!")

print("For movement simply choose direction to move in. Also walls will block you when trying to move.")

print("The Stick gives you a +1 attack bonus and the other item you may get gives a +4 in attack bonus.")

print("You start with your weapon being the stick.")

print("You don't start with anything in your inventory.")

print("The weapon you can get will automatically go into your inventory after you collect it.")

print("")

print("You have been trapped in a cave and you need to get the key from the Boss to escape!")

InventoryList = []

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

DamageAndCombatDoneList = ["", "", "", ""]

PlayerStatPoints = 0
PlayerHasDoneCombat = False
PlayerHasDefended = False
EquippedItem = "Stick"
PlayerStatHealth = 6
PlayerStatDamage = 1
PlayerStatDefense = 1

FirstEnemyHealth = 6
FirstEnemyDamage = 2
FirstEnemyDefense = 0
FirstEnemyDefeated = False

SecondEnemyHealth = 6
SecondEnemyDamage = 4
SecondEnemyDefense = 0
SecondEnemyDefeated = False

ThirdEnemyHealth = 8
ThirdEnemyDamage = 5
ThirdEnemyDefense = 4
ThirdEnemyDefeated = False

FinalBossHealth = 12
FinalBossDamage = 8
FinalBossDefense = 6
FinalBossDefeated = False

EnemyDecision = 0

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

def Movement(PlayerMoveDirectionFVar, CurrentPlayerSpaceFVar, GameMapFVar):
    PlayerMapSpace = [-1,-1]
    if PlayerMoveDirectionFVar.lower() == "left":
        PlayerMapSpace = [CurrentPlayerSpaceFVar[0], CurrentPlayerSpaceFVar[1] - 1]
    elif PlayerMoveDirectionFVar.lower() == "right":
        PlayerMapSpace = [CurrentPlayerSpaceFVar[0], CurrentPlayerSpaceFVar[1] + 1]
    elif PlayerMoveDirectionFVar.lower() == "up":
        PlayerMapSpace = [CurrentPlayerSpaceFVar[0] - 1, CurrentPlayerSpaceFVar[1]]
    elif PlayerMoveDirectionFVar.lower() == "down":
        PlayerMapSpace = [CurrentPlayerSpaceFVar[0] + 1, CurrentPlayerSpaceFVar[1]]
    if PlayerCanMoveInSpace(PlayerMapSpace, GameMapFVar):
        return PlayerMapSpace
    else:
        print(f"The direction {PlayerMoveDirectionFVar} moves into the boundry of the cave or a wall please try again.")
        return CurrentPlayerSpaceFVar
    

def Combat(EnemyHealthFVar, PlayerHealthFVar, EnemyDamageFVar, PlayerDamageFVar, EnemyDefenseFVar, PlayerDefenseFVar, PlayerDefeatedFVar, EnemyDefeatedFVar):
    DamageAndCombatDoneListFVar = [None, None, None, None]
    PlayerHasDoneCombatFVar = False
    print(EnemyHealthFVar)
    print(PlayerHealthFVar)
    print(DamageAndCombatDoneListFVar)
    if EnemyHealthFVar <= 0:
        EnemyDefeatedFVar = "Enemy Dead"
    elif PlayerHealthFVar <= 0:
        PlayerDefeatedFVar = "Player Dead"
    if EnemyDefeatedFVar == "Enemy Dead":
        PlayerHasDoneCombatFVar = True
        DamageAndCombatDoneListFVar[0] = PlayerHasDoneCombatFVar
        DamageAndCombatDoneListFVar[1] = EnemyDefeatedFVar
        DamageAndCombatDoneListFVar[2] = "Player"
        return DamageAndCombatDoneListFVar
    elif PlayerDefeatedFVar == "Player Dead":
        PlayerHasDoneCombatFVar = True
        DamageAndCombatDoneListFVar[0] = PlayerHasDoneCombatFVar
        DamageAndCombatDoneListFVar[1] = PlayerDefeatedFVar
        DamageAndCombatDoneListFVar[2] = "Enemy"
        return DamageAndCombatDoneListFVar
    elif EnemyDefeatedFVar != "Enemy Dead" and PlayerDefeatedFVar != "Player Dead":
        PlayerCombatDecision = str(input(f"Do you want to Attack, Defend, or dodge an attack? (To dodge an attack type Dodge) Also Your health is at {PlayerHealthFVar} The enemy's health is at {EnemyHealthFVar}: "))
        PlayerHasDoneCombatFVar = False
        PlayerHasDefendedFVar = False
        if PlayerCombatDecision.lower() == "attack":
            EnemyDecision = random.randint(1, 6)
            if EnemyDecision <= 2:
                EnemyDodgedAttack = random.randint(1, 10)
                if EnemyDodgedAttack <= 2:
                    print("The enemy dodged the attack.")
                    PlayerHasDoneCombatFVar = True
                    DamageAndCombatDoneListFVar[0] = PlayerHasDoneCombatFVar
                    DamageAndCombatDoneListFVar[1] = EnemyHealthFVar
                    DamageAndCombatDoneListFVar[2] = PlayerHealthFVar
                    DamageAndCombatDoneListFVar[3] = "Ran Away"
                    return DamageAndCombatDoneListFVar
                elif EnemyDodgedAttack >= 3:
                    EnemyDamageReduction = PlayerDamageFVar - EnemyDefenseFVar
                    EnemyHealthFVar -= EnemyDamageReduction
                    print(f"The enemy has defended but you have still hit the enemy for {EnemyDamageReduction} damage and the enemy now has {EnemyHealthFVar} health!")
                    PlayerHasDoneCombatFVar = True
                    DamageAndCombatDoneListFVar[0] = PlayerHasDoneCombatFVar
                    DamageAndCombatDoneListFVar[1] = EnemyHealthFVar
                    DamageAndCombatDoneListFVar[2] = "Enemy"
                    return DamageAndCombatDoneListFVar
            elif EnemyDecision >= 4:
                EnemyHealthFVar -= PlayerDamageFVar
                EnemyHealthFVar = max(EnemyHealthFVar, 0)
                print(f"You have hit the enemy for {PlayerDamageFVar} damage and the enemy now has {EnemyHealthFVar} health!")
                if EnemyHealthFVar == 0:
                    pass
                elif EnemyHealthFVar > 0:
                    PlayerHealthFVar -= EnemyDamageFVar
                    PlayerHealthFVar = max(PlayerHealthFVar, 0)
                    print(f"The enemy has hit you for {EnemyDamageFVar} damage and you now have {PlayerHealthFVar} health.")
                PlayerHasDoneCombatFVar = True
                DamageAndCombatDoneListFVar[0] = PlayerHasDoneCombatFVar
                DamageAndCombatDoneListFVar[1] = EnemyHealthFVar
                DamageAndCombatDoneListFVar[2] = PlayerHealthFVar
                DamageAndCombatDoneListFVar[3] = "Both"
                return DamageAndCombatDoneListFVar
            elif EnemyDecision == 3:
                EnemyWasAbleToRunAwayFVar = random.randint(1, 2)
                if EnemyWasAbleToRunAwayFVar == 1:
                    EnemyHealthFVar -= PlayerDamageFVar
                    print(f"You have hit the enemy for {PlayerDamageFVar} damage and the enemy now has {EnemyHealthFVar} health!")
                    PlayerHasDoneCombatFVar = True
                    DamageAndCombatDoneListFVar[0] = PlayerHasDoneCombatFVar
                    DamageAndCombatDoneListFVar[1] = EnemyHealthFVar
                    DamageAndCombatDoneListFVar[2] = "Enemy"
                    return DamageAndCombatDoneListFVar
                elif EnemyWasAbleToRunAwayFVar == 2:
                    print("The enemy dodged the attack.")
                    EnemyRanAway = "Ran Away"
                    PlayerHasDoneCombatFVar = True
                    DamageAndCombatDoneListFVar[0] = PlayerHasDoneCombatFVar
                    DamageAndCombatDoneListFVar[1] = EnemyHealthFVar
                    DamageAndCombatDoneListFVar[2] = PlayerHealthFVar
                    DamageAndCombatDoneListFVar[3] = EnemyRanAway
                    return DamageAndCombatDoneListFVar
            else:
                print("An unexpected error has occurred please try again")
        elif PlayerCombatDecision.lower() == "defend":
            PlayerDodgedAttack = random.randint(1, 10)
            if PlayerDodgedAttack >= 3:
                PlayerDamageReduction = EnemyDamageFVar - PlayerDefenseFVar
                PlayerHealthFVar -= PlayerDamageReduction
                print(f"You have successfully defended and the enemy only did {PlayerDamageReduction} damage! and you now have {PlayerHealthFVar} health.")
                PlayerHasDefendedFVar = True
                DamageAndCombatDoneListFVar[0] = PlayerHasDefendedFVar
                DamageAndCombatDoneListFVar[1] = PlayerHealthFVar
                DamageAndCombatDoneListFVar[2] = "Player"
                return DamageAndCombatDoneListFVar
            elif PlayerDodgedAttack <= 2:
                print("You dodged their attack!")
                PlayerHasDefendedFVar = True
                DamageAndCombatDoneListFVar.append(PlayerHasDefendedFVar)
                return DamageAndCombatDoneListFVar
        elif PlayerCombatDecision.lower() == "dodge":
            PlayerWasAbleToRunAway = random.randint(1, 2)
            if PlayerWasAbleToRunAway == 1:
                PlayerHealthFVar -= EnemyDamageFVar
                print(f"You have failed to Dodge and the enemy has hit you for {EnemyDamageFVar} damage. and you now have {PlayerHealthFVar} health.")
                PlayerHasDoneCombatFVar = True
                DamageAndCombatDoneListFVar[0] = PlayerHasDoneCombatFVar
                DamageAndCombatDoneListFVar[1] = PlayerHealthFVar
                DamageAndCombatDoneListFVar[2] = "Player"
                return DamageAndCombatDoneListFVar
            elif PlayerWasAbleToRunAway == 2:
                print("You have successfully Dodged!")
                PlayerRanAway = "Ran Away"
                PlayerHasDoneCombatFVar = True
                DamageAndCombatDoneListFVar[0] = PlayerHasDoneCombatFVar
                DamageAndCombatDoneListFVar[1] = EnemyHealthFVar
                DamageAndCombatDoneListFVar[2] = PlayerHealthFVar
                DamageAndCombatDoneListFVar[3] = PlayerRanAway
                return DamageAndCombatDoneListFVar
        else:
            print("Unexpected Error try again.")
            PlayerHasDoneCombatFVar = True
            DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
            DamageAndCombatDoneListFVar.append("No One Died")
            return DamageAndCombatDoneListFVar

def FinalBossCombat(EnemyHealthFVar2, PlayerHealthFVar2, EnemyDamageFVar2, PlayerDamageFVar2, EnemyDefenseFVar2, PlayerDefenseFVar2, FinalBossDefeatedFVar, PlayerDefeatedFVar2):
    DamageAndCombatDoneListFVar2 = []
    PlayerHasDoneCombatFVar2 = False
    if EnemyHealthFVar2 <= 0:
        FinalBossDefeatedFVar = "Enemy Dead"
    elif PlayerHealthFVar2 <= 0:
        PlayerDefeatedFVar2 = "Player Dead"
    if FinalBossDefeatedFVar == "Enemy Dead":
        PlayerHasDoneCombatFVar2 = True
        DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
        DamageAndCombatDoneListFVar2.append(FinalBossDefeatedFVar)
        DamageAndCombatDoneListFVar2.append("Player")
        return DamageAndCombatDoneListFVar2
    elif PlayerDefeatedFVar2 == "Player Dead":
        PlayerHasDoneCombatFVar2 = True
        DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
        DamageAndCombatDoneListFVar2.append(PlayerDefeatedFVar2)
        DamageAndCombatDoneListFVar2.append("Enemy")
        return DamageAndCombatDoneListFVar2
    elif FinalBossDefeatedFVar != "Enemy Dead" and PlayerDefeatedFVar2 != "Player Dead":
        PlayerCombatDecision = str(input(f"Do you want to Attack, Defend, or dodge an attack? (To dodge an attack type Dodge) Also Your health is at {PlayerHealthFVar2} The Boss's health is at {EnemyHealthFVar2}: "))
        PlayerHasDoneCombatFVar2 = False
        PlayerHasDefendedFVar2 = False
        if PlayerCombatDecision.lower() == "attack":
            FinalBossDecision = random.randint(1, 5)
            if FinalBossDecision <= 2:
                FinalBossDodgedAttack = random.randint(1, 10)
                if FinalBossDodgedAttack <= 2:
                    print("The Boss dodged the attack!")
                    PlayerHasDoneCombatFVar2 = True
                    DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
                    DamageAndCombatDoneListFVar2.append(EnemyHealthFVar2)
                    DamageAndCombatDoneListFVar2.append(PlayerHealthFVar2)
                    DamageAndCombatDoneListFVar2.append("Ran Away")
                    return DamageAndCombatDoneListFVar2
                elif FinalBossDodgedAttack >= 3:
                    EnemyDamageReductionFVar = PlayerDamageFVar2 - EnemyDefenseFVar2
                    EnemyHealthFVar2 -= EnemyDamageReductionFVar
                    print(f"The Boss has defended but you have still hit the Boss for {EnemyDamageReductionFVar} damage and the Boss now has {EnemyHealthFVar2} health!")
                    PlayerHasDoneCombatFVar2 = True
                    DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
                    DamageAndCombatDoneListFVar2.append(EnemyHealthFVar2)
                    DamageAndCombatDoneListFVar2.append("Enemy")
                    return DamageAndCombatDoneListFVar2
            elif FinalBossDecision >= 3:
                EnemyHealthFVar2 -= PlayerDamageFVar2
                EnemyHealthFVar2 = max(EnemyHealthFVar2, 0)
                print(f"You have hit the Boss for {PlayerDamageFVar2} damage and the Boss now has {EnemyHealthFVar2} health!")
                if EnemyHealthFVar2 == 0:
                    pass
                elif EnemyHealthFVar2 > 0:
                    PlayerHealthFVar2 -= EnemyDamageFVar2
                    PlayerHealthFVar = max(PlayerHealthFVar, 0)
                    print(f"The Boss has hit you for {EnemyDamageFVar2} damage and you now have {PlayerHealthFVar2} health.")
                PlayerHasDoneCombatFVar2 = True
                DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
                DamageAndCombatDoneListFVar2.append(EnemyHealthFVar2)
                DamageAndCombatDoneListFVar2.append(PlayerHealthFVar2)
                DamageAndCombatDoneListFVar2.append("Both")
                return DamageAndCombatDoneListFVar2
        elif PlayerCombatDecision.lower() == "defense":
            PlayerDodgedAttack = random.randint(1, 10)
            if PlayerDodgedAttack >= 3:
                PlayerDamageReductionFVar = EnemyDamageFVar2 - PlayerDefenseFVar2
                PlayerHealthFVar2 -= PlayerDamageReductionFVar
                print(f"You have successfully defended and the enemy only did {PlayerDamageReductionFVar} damage! and you now have {PlayerHealthFVar2} health.")
                PlayerHasDefendedFVar2 = True
                DamageAndCombatDoneListFVar2.append(PlayerHasDefendedFVar2)
                DamageAndCombatDoneListFVar2.append(PlayerHealthFVar2)
                DamageAndCombatDoneListFVar2.append("Player")
                return DamageAndCombatDoneListFVar2
            elif PlayerDodgedAttack <= 2:
                print("You dodged their attack!")
                PlayerHasDefendedFVar2 = True
                DamageAndCombatDoneListFVar2.append(PlayerHasDefendedFVar2)
                return DamageAndCombatDoneListFVar2
        elif PlayerCombatDecision.lower() == "dodge":
            PlayerWasAbleToRunAway = random.randint(1, 2)
            if PlayerWasAbleToRunAway == 1:
                PlayerHealthFVar2 -= EnemyDamageFVar2
                print(f"You have failed to dodge and the Boss has hit you for {EnemyDamageFVar2} damage. and you now have {PlayerHealthFVar2} health.")
                PlayerHasDoneCombatFVar2 = True
                DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
                DamageAndCombatDoneListFVar2.append(PlayerHealthFVar2)
                DamageAndCombatDoneListFVar2.append("Player")
                return DamageAndCombatDoneListFVar2
            elif PlayerWasAbleToRunAway == 2:
                print("You have successfully dodged!")
                PlayerHasDoneCombatFVar2 = True
                DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
                DamageAndCombatDoneListFVar2.append(EnemyHealthFVar2)
                DamageAndCombatDoneListFVar2.append(PlayerHealthFVar2)
                DamageAndCombatDoneListFVar2.append("Both")
                return DamageAndCombatDoneListFVar2
        else:
            print("Unexpected Error try again.")
            PlayerHasDoneCombatFVar2 = True
            DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
            DamageAndCombatDoneListFVar2.append("No One Died")
            return DamageAndCombatDoneListFVar2

ChestList1 = ["", ""]
ChestList2 = ["", ""]
ChestList3 = ["", ""]
ChestList4 = ["", ""]
ChestList5 = ["", ""]

def ChestOpener(CurrentPlayerSpaceFVar, ChestOpened):
    ChestFVarList = []
    PointAmountGiven = 0
    if CurrentPlayerSpaceFVar == "Chest1":
        if ChestOpened == False:
            print("You have found the first chest inside it gives you one stat point!")
            PointAmountGiven = 1
            ChestFVarList = [PointAmountGiven, True]
            return ChestFVarList
        elif ChestOpened == True:
            pass
    if CurrentPlayerSpaceFVar == "Chest2":
        if ChestOpened == False:
            print("You have found the second chest inside it gives you two stat points!")
            PointAmountGiven = 2
            ChestFVarList = [PointAmountGiven, True]
            return ChestFVarList
        elif ChestOpened == True:
            pass
    if CurrentPlayerSpaceFVar == "Chest3":
        if ChestOpened == False:
            print("You have found the third chest inside it gives you three stat points!")
            PointAmountGiven = 3
            ChestFVarList = [PointAmountGiven, True]
            return ChestFVarList
        elif ChestOpened == True:
            pass
    if CurrentPlayerSpaceFVar == "Chest4":
        if ChestOpened == False:
            print("You have found the fourth chest inside it gives you four stat points!")
            PointAmountGiven = 4
            ChestFVarList = [PointAmountGiven, True]
            return ChestFVarList
        elif ChestOpened == True:
            pass
    if CurrentPlayerSpaceFVar == "Chest5":
        if ChestOpened == False:
            print("You have found the fifth chest inside it gives you a sword!!!")
            ChestFVarList = ["Sword", True]
            return ChestFVarList
        elif ChestOpened == True:
            pass

GameMapRow1 = [Space1, Space2, Space3, Space4, Space5]
GameMapRow2 = [Space6, Space7, Space8, Space9, Space10]
GameMapRow3 = [Space11, Space12, Space13, Space14, Space15]
GameMapRow4 = [Space16, Space17, Space18, Space19, Space20]
GameMapRow5 = [Space21, Space22, Space23, Space24, Space25]

GameMapCollumn1 = [Space1, Space6, Space11, Space16, Space21]
GameMapCollumn2 = [Space2, Space7, Space12, Space17, Space22]
GameMapCollumn3 = [Space3, Space8, Space13, Space18, Space23]
GameMapCollumn4 = [Space4, Space9, Space14, Space19, Space24]
GameMapCollumn5 = [Space5, Space10, Space15, Space20, Space25]

GameMap = [GameMapRow1, GameMapRow2, GameMapRow3, GameMapRow4, GameMapRow5]

CurrentPlayerSpace = [0, 0]

PlayerMapSpace = ""
PlayerKeyHolder = ""

FirstChestOpened = False
SecondChestOpened = False
ThirdChestOpened = False
FourthChestOpened = False
FifthChestOpened = False
PlayerDefeated = False
PlayerHealth = int(PlayerStatHealth)

print(f"You have been started at {GetMapSpace(CurrentPlayerSpace, GameMap)}!")

loop_num = 0
while True:
    loop_num += 1
    print(f'Game Loop {loop_num}')

    GameMapRow1 = [Space1, Space2, Space3, Space4, Space5]
    GameMapRow2 = [Space6, Space7, Space8, Space9, Space10]
    GameMapRow3 = [Space11, Space12, Space13, Space14, Space15]
    GameMapRow4 = [Space16, Space17, Space18, Space19, Space20]
    GameMapRow5 = [Space21, Space22, Space23, Space24, Space25]

    GameMap = [GameMapRow1, GameMapRow2, GameMapRow3, GameMapRow4, GameMapRow5]

    if EquippedItem == "Stick":
        WeaponStatDamage = 1
    elif EquippedItem == "Sword":
        WeaponStatDamage = 4

    DamageAndCombatDoneList = ["PlaceHolder1", "PlaceHolder2", "PlaceHolder3", "PlaceHolder4"]
    PlayerDamage = PlayerStatDamage + WeaponStatDamage
    PlayerDefense = PlayerStatDefense

    for x in GameMap:
        print(x)

    if PlayerKeyHolder == "Key" and CurrentPlayerSpace == [0, 0]:
        print("You have won the game congrats!")
        break

    if GetMapSpace(CurrentPlayerSpace, GameMap) == "Chest1":
        ChestList1 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), FirstChestOpened)
        if FirstChestOpened == False:
            PlayerStatPoints += ChestList1[0]
            FirstChestOpened = ChestList1[1]
            Space21 = "Space21"
        elif FirstChestOpened == True:
            pass
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "Chest2":
        ChestList2 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), SecondChestOpened)
        if SecondChestOpened == False:
            PlayerStatPoints += ChestList2[0]
            SecondChestOpened = ChestList2[1]
            Space23 = "Space23"
        if SecondChestOpened == True:
            pass
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "Chest3":
        ChestList3 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), ThirdChestOpened)
        if ThirdChestOpened == False:
            PlayerStatPoints += ChestList3[0]
            ThirdChestOpened = ChestList3[1]
            Space15 = "Space15"
        if ThirdChestOpened == True:
            pass
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "Chest4":
        ChestList4 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), FourthChestOpened)
        if FourthChestOpened == False:
            PlayerStatPoints += ChestList4[0]
            FourthChestOpened = ChestList4[1]
            Space5 = "Space5"
        if FourthChestOpened == True:
            pass
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "Chest5":
        ChestList5 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), FifthChestOpened)
        if FifthChestOpened == False:
            InventoryList.append(ChestList5[0])
            FifthChestOpened = ChestList5[1]
            Space13 = "Space13"
        if FifthChestOpened == True:
            pass
    
    PlayerDecision = str(input(f"Do you want to move, check your inventory or check / use your stats?? (Type Move and also the direction you want to move with a space in between for movement, Inventory for inventory checking, Stats for Stats checking / using them, Health to check your current health, and Item to check the current item you have equipped) Also you are at {GetMapSpace(CurrentPlayerSpace, GameMap)}: "))

    PlayerDecision = PlayerDecision.split()
    if PlayerDecision[0].lower() == "move":
        PlayerMoveDirection = PlayerDecision[1]
        CurrentPlayerSpace = Movement(PlayerMoveDirection, CurrentPlayerSpace, GameMap)
        PlayerMapSpace = GetMapSpace(CurrentPlayerSpace, GameMap)
        print(f"You have moved to {PlayerMapSpace}!")
    elif PlayerDecision[0].lower() == "inventory":
        while True:
            PlayerInventoryAction = str(input("Do you want to swap the item you currently have or Exit your inventory? (Say Swap to swap your stick and the item you will get and Exit to exit the inventory): "))
            if PlayerInventoryAction.lower() == "swap":
                if InventoryList != []:
                    PlayerSwapAction = str(input("What item do you want to swap?: "))
                    if PlayerSwapAction.lower() == "sword":
                        if EquippedItem == "Sword":
                            print("You can't swap out your sword for your sword.")
                            continue
                        elif EquippedItem == "Stick":
                            EquippedItem = "Sword"
                            InventoryList.remove("Sword")
                            print("You have succesfully swapped out your stick for your sword!")
                        elif EquippedItem == "Nothing":
                            EquippedItem = ("Sword")
                            InventoryList.remove("Sword")
                            print("You have swapped out nothing for your stick so you basically just took it out!")
                            continue
                        else:
                            print("Unexpected error try again.")
                            continue
                    elif PlayerSwapAction.lower() == "stick":
                        if EquippedItem == "Stick":
                            print("You can't swap out your stick for your stick.")
                            continue
                        elif EquippedItem == "Sword":
                            EquippedItem = "Stick"
                            InventoryList.remove("Stick")
                            InventoryList.append("Sword")
                            print("You have succesfully swapped out your sword for your stick!")
                        elif EquippedItem == "Nothing":
                            EquippedItem = ("Stick")
                            InventoryList.remove("Stick")
                            print("You have swapped out nothing for your stick so you basically just took it out!")
                            continue
                        else:
                            print("Unexpected error try again.")
                            continue
                elif InventoryList == []:
                    print("You can't swap anything you don't have anything in your inventory.")
                    continue
            elif PlayerInventoryAction.lower() == "exit":
                print("Hope you had a succesfull inventory use!")
                break
    elif PlayerDecision[0].lower() == "stats":
        while True:
            PlayerStatAction = str(input(f"Do you want to check your stats, use your stat points, or exit your stats? (To check stats type Stats, to use stat points type Points, to exit type Exit) You currently have {PlayerStatPoints} Stat Points: "))
            if PlayerStatAction.lower() == "stats":
                print(f"These are your current stats Health is {PlayerStatHealth}, Damage is {PlayerStatDamage}, and Defense is {PlayerStatDefense}.")
            elif PlayerStatAction.lower() == "points":
                if PlayerStatPoints > 0:
                        PlayerStatDecision = str(input(f"What stat do you want to add to? Also you currently have This many stat points {PlayerStatPoints}. (Type Damage for damage, Health for health, and Defense for defense): "))
                        if PlayerStatDecision.lower() == "damage":
                            print(f"How much do you want to add to Damage? You have {PlayerStatPoints} point(s).")
                            DamagePointAdd = int(input("Number: "))
                            if DamagePointAdd > PlayerStatPoints:
                                print("You can't add more points than you have! Please Decide the number of points you want to add again.")
                                DamagePointAdd = int(input("Number: "))
                                PlayerStatDamage += DamagePointAdd
                                PlayerStatPoints -= DamagePointAdd
                                print(f"You have successfully added {DamagePointAdd} points to damage!")
                                DamagePointAdd = 0
                            elif DamagePointAdd <= PlayerStatPoints:
                                PlayerStatDamage += DamagePointAdd
                                PlayerStatPoints -= DamagePointAdd
                                print(f"You have successfully added {DamagePointAdd} points to damage!")
                                DamagePointAdd = 0
                        if PlayerStatDecision.lower() == "health":
                            print(f"How much do you want to add to Health? You have {PlayerStatPoints} point(s).")
                            HealthPointAdd = int(input("Number: "))
                            if HealthPointAdd > PlayerStatPoints:
                                print("You can't add more points than you have! Please Decide the number of points you want to add again.")
                                HealthPointAdd = int(input("Number: "))
                                PlayerStatHealth += HealthPointAdd
                                PlayerStatPoints -= HealthPointAdd
                                PlayerHealth = int(PlayerStatHealth)
                                print(f"You have successfully added {HealthPointAdd} points to health!")
                                HealthPointAdd = 0
                            elif HealthPointAdd <= PlayerStatPoints:
                                PlayerStatHealth += HealthPointAdd
                                PlayerStatPoints -= HealthPointAdd
                                print(f"You have successfully added {HealthPointAdd} points to health!")
                                HealthPointAdd = 0
                        if PlayerStatDecision.lower() == "defense":
                            print("How much do you want to add to Defense?")
                            DefensePointAdd = int(input("Number: "))
                            if DefensePointAdd > PlayerStatPoints:
                                print("You can't add more points than you have! Please Decide the number of points you want to add again.")
                                DefensePointAdd = int(input("Number: "))
                                PlayerStatDefense += DefensePointAdd
                                PlayerStatPoints -= DefensePointAdd
                                print(f"You have successfully added {DefensePointAdd} points to defense!")
                                DefensePointAdd = 0
                            elif DefensePointAdd <= PlayerStatPoints:
                                PlayerStatDefense += DefensePointAdd
                                PlayerStatPoints -= DefensePointAdd
                                print(f"You have successfully added {DefensePointAdd} points to defense!")
                                DefensePointAdd = 0
            elif PlayerStatAction.lower() == "exit":
                print("Hope you had a succesful time using stats!")
                break
    elif PlayerDecision[0].lower() == "health":
        print(f"This is your current health! {PlayerHealth}")
    elif PlayerDecision[0].lower() == "item":
        print(f"You currently have {EquippedItem} equipped!")
    if GetMapSpace(CurrentPlayerSpace, GameMap) == "Enemy1":
        if FirstEnemyDefeated == False:
            print("You encountered Enemy number 1! Time to fight them.")
            while True:
                while DamageAndCombatDoneList[1] != "Enemy Dead" and DamageAndCombatDoneList[1] != "Player Dead":
                    print(f"ENEMY 1 BUG: PlayerHealth = {PlayerHealth}")
                    DamageAndCombatDoneList = Combat(FirstEnemyHealth, PlayerHealth, FirstEnemyDamage, PlayerDamage, FirstEnemyDefense, PlayerDefense, PlayerDefeated, FirstEnemyDefeated)
                    if DamageAndCombatDoneList[0] != True:
                        continue
                    elif DamageAndCombatDoneList[0] == True:
                        if len(DamageAndCombatDoneList) >= 3:
                            if DamageAndCombatDoneList[2] == "Enemy":
                                FirstEnemyHealth = DamageAndCombatDoneList[1]
                                continue
                            elif DamageAndCombatDoneList[2] == "Player":
                                PlayerHealth = DamageAndCombatDoneList[1]
                                continue
                            elif DamageAndCombatDoneList[3] == "Both":
                                FirstEnemyHealth = DamageAndCombatDoneList[1]
                                PlayerHealth = DamageAndCombatDoneList[2]
                                continue
                            elif DamageAndCombatDoneList[3] == "Ran Away":
                                FirstEnemyHealth = DamageAndCombatDoneList[1]
                                PlayerHealth = DamageAndCombatDoneList[2]
                                continue
                else:
                    if DamageAndCombatDoneList[1] == "Enemy Dead":
                        FirstEnemyDefeated = True
                        print("You have successfully defeated Enemy1! and gained 8 stat points because of it!")
                        PlayerStatPoints += 2
                        Space2 = "Space2"
                        break
                    elif DamageAndCombatDoneList[1] == "Player Dead":
                        print("You have sadly been defeated by Enemy1")
                        FirstEnemyHealth = 6
                        PlayerDefeated = True
                if FirstEnemyDefeated == True:
                    break
                elif PlayerDefeated == True:
                    PlayerDefeated = False
                    CurrentPlayerSpace = [0, 0]
                    PlayerHealth = int(PlayerStatHealth)
                    break
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "Enemy2":
        if SecondEnemyDefeated == False:
            print("You encountered Enemy number 2! Time to fight them.")
            while True:
                while DamageAndCombatDoneList[1] != "Enemy Dead" and DamageAndCombatDoneList[1] != "Player Dead":
                    print(f'ENEMY 2 BUG: DamageAndCombatDoneList Before = {DamageAndCombatDoneList}')
                    DamageAndCombatDoneList = Combat(SecondEnemyHealth, PlayerHealth, SecondEnemyDamage, PlayerDamage, SecondEnemyDefense, PlayerDefense, PlayerDefeated, SecondEnemyDefeated)
                    print(f'ENEMY 2 BUG: DamageAndCombatDoneList After = {DamageAndCombatDoneList}')
                    if DamageAndCombatDoneList[0] != True:
                        continue
                    elif DamageAndCombatDoneList[0] == True:
                        if DamageAndCombatDoneList[2] == "Enemy":
                            SecondEnemyHealth = DamageAndCombatDoneList[1]
                        elif DamageAndCombatDoneList[2] == "Player":
                            PlayerHealth = DamageAndCombatDoneList[1]
                        elif DamageAndCombatDoneList[3] == "Both":
                            SecondEnemyHealth = DamageAndCombatDoneList[1]
                            PlayerHealth = DamageAndCombatDoneList[2]
                        elif DamageAndCombatDoneList[3] == "Ran Away":
                            SecondEnemyHealth = DamageAndCombatDoneList[1]
                            PlayerHealth = DamageAndCombatDoneList[2]
                else:
                    if DamageAndCombatDoneList[1] == "Enemy Dead":
                        SecondEnemyDefeated = True
                        print("You have successfully defeated Enemy2!")
                        PlayerStatPoints += 2
                        Space17 = "Space17"
                        break
                    elif DamageAndCombatDoneList[1] == "Player Dead":
                        PlayerDefeated = True
                        print("You have sadly been defeated by Enemy2")
                        SecondEnemyHealth = 6
                if SecondEnemyDefeated == True:
                    break
                elif PlayerDefeated == True:
                    PlayerDefeated = False
                    CurrentPlayerSpace = [0, 0]
                    PlayerHealth = int(PlayerStatHealth)
                    break
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "Enemy3":
        if ThirdEnemyDefeated == False:
            print("You encountered Enemy number 3! Time to fight them.")
            while True:
                while DamageAndCombatDoneList[1] != "Enemy Dead" and DamageAndCombatDoneList[1] != "Player Dead":
                    DamageAndCombatDoneList = Combat(ThirdEnemyHealth, PlayerHealth, ThirdEnemyDamage, PlayerDamage, ThirdEnemyDefense, PlayerDefense, PlayerDefeated, ThirdEnemyDefeated)
                    if DamageAndCombatDoneList[0] != True:
                        continue
                    elif DamageAndCombatDoneList[0] == True:
                        if DamageAndCombatDoneList[2] == "Enemy":
                            ThirdEnemyHealth = DamageAndCombatDoneList[1]
                        elif DamageAndCombatDoneList[2] == "Player":
                            PlayerHealth = DamageAndCombatDoneList[1]
                        elif DamageAndCombatDoneList[3] == "Both":
                            ThirdEnemyHealth = DamageAndCombatDoneList[1]
                            PlayerHealth = DamageAndCombatDoneList[2]
                        elif DamageAndCombatDoneList[3] == "Ran Away":
                            ThirdEnemyHealth = DamageAndCombatDoneList[1]
                            PlayerHealth = DamageAndCombatDoneList[2]
                else:
                    if DamageAndCombatDoneList[1] == "Enemy Dead":
                        ThirdEnemyDefeated = True
                        print("You have successfully defeated Enemy3!")
                        PlayerStatPoints += 4
                        Space19 = "Space19"
                        break
                    elif DamageAndCombatDoneList[1] == "Player Dead":
                        print("You have sadly been defeated by Enemy3")
                        ThirdEnemyHealth = 8
                        PlayerDefeated = True
                if ThirdEnemyDefeated == True:
                    break
                elif PlayerDefeated == True:
                    PlayerDefeated = False
                    CurrentPlayerSpace = [0, 0]
                    PlayerHealth = int(PlayerStatHealth)
                    break
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "FinalBoss":
        if FinalBossDefeated == False and FirstEnemyDefeated == True and SecondEnemyDefeated == True and ThirdEnemyDefeated == True:
            print("You encountered The Final Boss the final battle is at hand.")
            while True:
                while DamageAndCombatDoneList[1] != "Enemy Dead" and DamageAndCombatDoneList[1] != "Player Dead":
                    DamageAndCombatDoneList = FinalBossCombat(FinalBossHealth, PlayerHealth, FinalBossDamage, PlayerDamage, FinalBossDefense, PlayerDefense, FinalBossDefeated, PlayerDefeated)
                    if DamageAndCombatDoneList[0] != True:
                        continue
                    elif DamageAndCombatDoneList[0] == True:
                        if DamageAndCombatDoneList[2] == "Enemy":
                            FinalBossHealth = DamageAndCombatDoneList[1]
                        elif DamageAndCombatDoneList[2] == "Player":
                            PlayerHealth = DamageAndCombatDoneList[1]
                        elif DamageAndCombatDoneList[3] == "Both":
                            FinalBossHealth = DamageAndCombatDoneList[1]
                            PlayerHealth = DamageAndCombatDoneList[2]
                        elif DamageAndCombatDoneList[3] == "Ran Away":
                            FinalBossHealth = DamageAndCombatDoneList[1]
                            PlayerHealth = DamageAndCombatDoneList[2]
                else:
                    if DamageAndCombatDoneList[1] == "Enemy Dead":
                        print("You have successfully defeated The Final Boss and got the exit key!!!")
                        PlayerKeyHolder = "Key"
                        FinalBossDefeated = True
                        Space25 = "Space25"
                        break
                    elif DamageAndCombatDoneList[1] == "Player Dead":
                        print("You have sadly been defeated by The Final Boss.")
                        FinalBossHealth = 12
                        PlayerDefeated = True
                if FinalBossDefeated == True:
                    break
                elif PlayerDefeated == True:
                    PlayerDefeated = False
                    CurrentPlayerSpace = [0, 0]
                    PlayerHealth = int(PlayerStatHealth)
                    break