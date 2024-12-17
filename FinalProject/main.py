#Max Holdaway Final Project

import random as random

for x in range(0, 21):
    print("")

print("You have been trapped in a cave and you need to get the key from the final boss to escape.")

print("")

print("For movement simply choose direction to move in. Also walls will block you when trying to move.")

print("The Stick gives you a +1 attack bonus and the other item you may get gives a +4 in attack bonus.")

print("You start with your weapon being the stick.")

print("You don't start with anything in your inventory.")

print("The weapon you can get will automatically go into your inventory after you collect it. But you still need to equip it in the menu.")

print("Numbers mean empty spaces.")

print("SX means start/exit space.")

print("[] are walls.")

print("FB means final boss.")

print("E followed by a number is an enemy.")

print("C followed by a number is a chest")

print("Damage increases how much damage your attacks do, health increase your max health, and shield increases how much you lower the enemy damage when you defend.")

print("Even if you die you have infinite lives. So this game simply takes time.")

print("Good luck and have fun!")

print("")

InventoryList = []

Space1 = "SX"
Space2 = "E1"
Space3 = "03"
Space4 = "04"
Space5 = "C4"
Space6 = "06"
Space7 = "[]"
Space8 = "08"
Space9 = "[]"
Space10 = "10"
Space11 = "11"
Space12 = "[]"
Space13 = "C5"
Space14 = "[]"
Space15 = "C3"
Space16 = "16"
Space17 = "E2"
Space18 = "18"
Space19 = "E3"
Space20 = "20"
Space21 = "C1"
Space22 = "[]"
Space23 = "C2"
Space24 = "[]"
Space25 = "FB"

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

SecondEnemyHealth = 8
SecondEnemyDamage = 4
SecondEnemyDefense = 2
SecondEnemyDefeated = False

ThirdEnemyHealth = 12
ThirdEnemyDamage = 6
ThirdEnemyDefense = 4
ThirdEnemyDefeated = False

FinalBossHealth = 20
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
        GetMapSpace(CurrentPlayerSpaceFVar, GameMapFVar).startswith('[]') 
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
        PlayerCombatDecision = str(input(f"Do you want to attack, defend, or dodge? \n Your health is at {PlayerHealthFVar} and the enemy's health is at {EnemyHealthFVar}: "))
        print("")
        print("")
        print("")
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
                    EnemyHealthFVar = max(EnemyHealthFVar, 0)
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
                    EnemyHealthFVar = max(EnemyHealthFVar, 0)
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
                PlayerHealthFVar = max(PlayerHealthFVar, 0)
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
                PlayerHealthFVar = max(PlayerHealthFVar, 0)
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
    DamageAndCombatDoneListFVar2 = [None, None, None, None]
    PlayerHasDoneCombatFVar2 = False
    if EnemyHealthFVar2 <= 0:
        FinalBossDefeatedFVar = "Enemy Dead"
    elif PlayerHealthFVar2 <= 0:
        PlayerDefeatedFVar2 = "Player Dead"
    if FinalBossDefeatedFVar == "Enemy Dead":
        PlayerHasDoneCombatFVar2 = True
        DamageAndCombatDoneListFVar2[0] = PlayerHasDoneCombatFVar2
        DamageAndCombatDoneListFVar2[1] = FinalBossDefeatedFVar
        DamageAndCombatDoneListFVar2[2] = "Player"
        return DamageAndCombatDoneListFVar2
    elif PlayerDefeatedFVar2 == "Player Dead":
        PlayerHasDoneCombatFVar2 = True
        DamageAndCombatDoneListFVar2[0] = PlayerHasDoneCombatFVar2
        DamageAndCombatDoneListFVar2[1] = PlayerDefeatedFVar2
        DamageAndCombatDoneListFVar2[2] = "Enemy"
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
                    DamageAndCombatDoneListFVar2[0] = PlayerHasDoneCombatFVar2
                    DamageAndCombatDoneListFVar2[1] = EnemyHealthFVar2
                    DamageAndCombatDoneListFVar2[2] = PlayerHealthFVar2
                    DamageAndCombatDoneListFVar2[3] = "Ran Away"
                    return DamageAndCombatDoneListFVar2
                elif FinalBossDodgedAttack >= 3:
                    EnemyDamageReductionFVar = PlayerDamageFVar2 - EnemyDefenseFVar2
                    EnemyHealthFVar2 -= EnemyDamageReductionFVar
                    EnemyHealthFVar2 = max(EnemyHealthFVar2, 0)
                    print(f"The Boss has defended but you have still hit the Boss for {EnemyDamageReductionFVar} damage and the Boss now has {EnemyHealthFVar2} health!")
                    PlayerHasDoneCombatFVar2 = True
                    DamageAndCombatDoneListFVar2[0] = PlayerHasDoneCombatFVar2
                    DamageAndCombatDoneListFVar2[1] = EnemyHealthFVar2
                    DamageAndCombatDoneListFVar2[2] = "Enemy"
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
                DamageAndCombatDoneListFVar2[0] = PlayerHasDoneCombatFVar2
                DamageAndCombatDoneListFVar2[1] = EnemyHealthFVar2
                DamageAndCombatDoneListFVar2[2] = PlayerHealthFVar2
                DamageAndCombatDoneListFVar2[3] = "Both"
                return DamageAndCombatDoneListFVar2
        elif PlayerCombatDecision.lower() == "shield":
            PlayerDodgedAttack = random.randint(1, 10)
            if PlayerDodgedAttack >= 3:
                PlayerDamageReductionFVar = EnemyDamageFVar2 - PlayerDefenseFVar2
                PlayerHealthFVar2 -= PlayerDamageReductionFVar
                print(f"You have successfully defended and the enemy only did {PlayerDamageReductionFVar} damage! and you now have {PlayerHealthFVar2} health.")
                PlayerHasDefendedFVar2 = True
                DamageAndCombatDoneListFVar2[0] = PlayerHasDefendedFVar2
                DamageAndCombatDoneListFVar2[1] = PlayerHealthFVar2
                DamageAndCombatDoneListFVar2[2] = "Player"
                return DamageAndCombatDoneListFVar2
            elif PlayerDodgedAttack <= 2:
                print("You dodged their attack!")
                PlayerHasDefendedFVar2 = True
                DamageAndCombatDoneListFVar2[0] = PlayerHasDefendedFVar2
                return DamageAndCombatDoneListFVar2
        elif PlayerCombatDecision.lower() == "dodge":
            PlayerWasAbleToRunAway = random.randint(1, 2)
            if PlayerWasAbleToRunAway == 1:
                PlayerHealthFVar2 -= EnemyDamageFVar2
                print(f"You have failed to dodge and the Boss has hit you for {EnemyDamageFVar2} damage. and you now have {PlayerHealthFVar2} health.")
                PlayerHasDoneCombatFVar2 = True
                DamageAndCombatDoneListFVar2[0] = PlayerHasDoneCombatFVar2
                DamageAndCombatDoneListFVar2[1] = PlayerHealthFVar2
                DamageAndCombatDoneListFVar2[2] = "Player"
                return DamageAndCombatDoneListFVar2
            elif PlayerWasAbleToRunAway == 2:
                print("You have successfully dodged!")
                PlayerHasDoneCombatFVar2 = True
                DamageAndCombatDoneListFVar2[0] = PlayerHasDoneCombatFVar2
                DamageAndCombatDoneListFVar2[1] = EnemyHealthFVar2
                DamageAndCombatDoneListFVar2[2] = PlayerHealthFVar2
                DamageAndCombatDoneListFVar2[3] = "Both"
                return DamageAndCombatDoneListFVar2
        else:
            print("Unexpected Error try again.")
            PlayerHasDoneCombatFVar2 = True
            DamageAndCombatDoneListFVar2[0] = PlayerHasDoneCombatFVar2
            DamageAndCombatDoneListFVar2[1] = "No One Died"
            return DamageAndCombatDoneListFVar2

ChestList1 = ["", ""]
ChestList2 = ["", ""]
ChestList3 = ["", ""]
ChestList4 = ["", ""]
ChestList5 = ["", ""]

def ChestOpener(CurrentPlayerSpaceFVar, ChestOpened):
    ChestFVarList = []
    PointAmountGiven = 0
    if CurrentPlayerSpaceFVar == "C1":
        if ChestOpened == False:
            print("You have found the first chest inside it gives you one stat point!")
            PointAmountGiven = 1
            ChestFVarList = [PointAmountGiven, True]
            return ChestFVarList
        elif ChestOpened == True:
            pass
    if CurrentPlayerSpaceFVar == "C2":
        if ChestOpened == False:
            print("You have found the second chest inside it gives you two stat points!")
            PointAmountGiven = 2
            ChestFVarList = [PointAmountGiven, True]
            return ChestFVarList
        elif ChestOpened == True:
            pass
    if CurrentPlayerSpaceFVar == "C3":
        if ChestOpened == False:
            print("You have found the third chest inside it gives you three stat points!")
            PointAmountGiven = 3
            ChestFVarList = [PointAmountGiven, True]
            return ChestFVarList
        elif ChestOpened == True:
            pass
    if CurrentPlayerSpaceFVar == "C4":
        if ChestOpened == False:
            print("You have found the fourth chest inside it gives you four stat points!")
            PointAmountGiven = 4
            ChestFVarList = [PointAmountGiven, True]
            return ChestFVarList
        elif ChestOpened == True:
            pass
    if CurrentPlayerSpaceFVar == "C5":
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

print(f"You have been started at {GetMapSpace(CurrentPlayerSpace, GameMap)}! Also the tutorial is above this so scroll up!")
while True:
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

    print("")

    if PlayerKeyHolder == "Key" and CurrentPlayerSpace == [0, 0]:
        print("You have won the game congrats!")
        break

    if GetMapSpace(CurrentPlayerSpace, GameMap) == "C1":
        ChestList1 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), FirstChestOpened)
        if FirstChestOpened == False:
            PlayerStatPoints += ChestList1[0]
            FirstChestOpened = ChestList1[1]
            Space21 = "21"
        elif FirstChestOpened == True:
            pass
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "C2":
        ChestList2 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), SecondChestOpened)
        if SecondChestOpened == False:
            PlayerStatPoints += ChestList2[0]
            SecondChestOpened = ChestList2[1]
            Space23 = "23"
        if SecondChestOpened == True:
            pass
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "C3":
        ChestList3 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), ThirdChestOpened)
        if ThirdChestOpened == False:
            PlayerStatPoints += ChestList3[0]
            ThirdChestOpened = ChestList3[1]
            Space15 = "15"
        if ThirdChestOpened == True:
            pass
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "C4":
        ChestList4 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), FourthChestOpened)
        if FourthChestOpened == False:
            PlayerStatPoints += ChestList4[0]
            FourthChestOpened = ChestList4[1]
            Space5 = "05"
        if FourthChestOpened == True:
            pass
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "C5":
        ChestList5 = ChestOpener(GetMapSpace(CurrentPlayerSpace, GameMap), FifthChestOpened)
        if FifthChestOpened == False:
            InventoryList.append(ChestList5[0])
            FifthChestOpened = ChestList5[1]
            Space13 = "13"
        if FifthChestOpened == True:
            pass
    
    PlayerDecision = str(input(f"To Move Type Move and the direction you want to go with a space in between \n To go into stats menu type Stats \n To go into inventory menu type inventory \n To check your health type Health \n To check which item you currently have type Item \n You are at {GetMapSpace(CurrentPlayerSpace, GameMap)}: "))

    PlayerDecision = PlayerDecision.split()
    if PlayerDecision[0].lower() == "move":
        PlayerMoveDirection = PlayerDecision[1]
        CurrentPlayerSpace = Movement(PlayerMoveDirection, CurrentPlayerSpace, GameMap)
        PlayerMapSpace = GetMapSpace(CurrentPlayerSpace, GameMap)
        print(f"You have moved to {PlayerMapSpace}!")
        print("")
    elif PlayerDecision[0].lower() == "inventory":
        while True:
            print("")
            PlayerInventoryAction = str(input(f"To swap out your current item type swap \n To exit the inventory type exit: "))
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
            print("")
            PlayerStatAction = str(input(f"Type points to use your stat points \n Type check to check your current stats \n Type exit to exit the stats menu \n You currently have {PlayerStatPoints} Stat Point(s): "))
            if PlayerStatAction.lower() == "check":
                print(f"These are your current stats Health is {PlayerStatHealth}, Damage is {PlayerDamage}, and Shield is {PlayerStatDefense}.")
            elif PlayerStatAction.lower() == "points":
                if PlayerStatPoints > 0:
                        PlayerStatDecision = str(input(f"Type Damage to add stats to damage \n Type Health to add points to health \n Type Shield to add points to your shield \n You currently have this many stat points {PlayerStatPoints}: "))
                        if PlayerStatDecision.lower() == "damage":
                            print("")
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
                            print("")
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
                        if PlayerStatDecision.lower() == "shield":
                            print("")
                            print(f"How much do you want to add to Shield? You have {PlayerStatPoints} point(s).")
                            DefensePointAdd = int(input("Number: "))
                            if DefensePointAdd > PlayerStatPoints:
                                print("You can't add more points than you have! Please Decide the number of points you want to add again.")
                                DefensePointAdd = int(input("Number: "))
                                PlayerStatDefense += DefensePointAdd
                                PlayerStatPoints -= DefensePointAdd
                                print(f"You have successfully added {DefensePointAdd} points to shield!")
                                DefensePointAdd = 0
                            elif DefensePointAdd <= PlayerStatPoints:
                                PlayerStatDefense += DefensePointAdd
                                PlayerStatPoints -= DefensePointAdd
                                print(f"You have successfully added {DefensePointAdd} points to shield!")
                                DefensePointAdd = 0
            elif PlayerStatAction.lower() == "exit":
                print("Hope you had a successful time using stats!")
                break
    elif PlayerDecision[0].lower() == "health":
        print(f"This is your current health! {PlayerHealth}")
    elif PlayerDecision[0].lower() == "item":
        print(f"You currently have {EquippedItem} equipped!")

    if GetMapSpace(CurrentPlayerSpace, GameMap) == "E1":
        if FirstEnemyDefeated == False:
            print("You encountered Enemy number 1! Time to fight them.")
            while True:
                while DamageAndCombatDoneList[1] != "Enemy Dead" and DamageAndCombatDoneList[1] != "Player Dead":
                    DamageAndCombatDoneList = Combat(FirstEnemyHealth, PlayerHealth, FirstEnemyDamage, PlayerDamage, FirstEnemyDefense, PlayerDefense, PlayerDefeated, FirstEnemyDefeated)
                    if DamageAndCombatDoneList[0] != True:
                        continue
                    elif DamageAndCombatDoneList[0] == True:
                        if len(DamageAndCombatDoneList) >= 3:
                            if DamageAndCombatDoneList[2] == "Enemy":
                                FirstEnemyHealth = DamageAndCombatDoneList[1]
                                continue
                            elif DamageAndCombatDoneList[2] == "Player" and DamageAndCombatDoneList[1] != "Enemy Dead":
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
                        print("You have successfully defeated Enemy1! and gained 2 stat points because of it!")
                        PlayerStatPoints += 2
                        Space2 = "02"
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
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "E2":
        if SecondEnemyDefeated == False:
            print("You encountered Enemy number 2! Time to fight them.")
            while True:
                while DamageAndCombatDoneList[1] != "Enemy Dead" and DamageAndCombatDoneList[1] != "Player Dead":
                    DamageAndCombatDoneList = Combat(SecondEnemyHealth, PlayerHealth, SecondEnemyDamage, PlayerDamage, SecondEnemyDefense, PlayerDefense, PlayerDefeated, SecondEnemyDefeated)
                    if DamageAndCombatDoneList[0] != True:
                        continue
                    elif DamageAndCombatDoneList[0] == True:
                        if DamageAndCombatDoneList[2] == "Enemy":
                            SecondEnemyHealth = DamageAndCombatDoneList[1]
                        elif DamageAndCombatDoneList[2] == "Player" and DamageAndCombatDoneList[1] != "Enemy Dead":
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
                        print("You have successfully defeated Enemy2! and gained 2 stat points because of it!")
                        PlayerStatPoints += 2
                        Space17 = "17"
                        break
                    elif DamageAndCombatDoneList[1] == "Player Dead":
                        PlayerDefeated = True
                        print("You have sadly been defeated by Enemy2")
                        SecondEnemyHealth = 8
                if SecondEnemyDefeated == True:
                    break
                elif PlayerDefeated == True:
                    PlayerDefeated = False
                    CurrentPlayerSpace = [0, 0]
                    PlayerHealth = int(PlayerStatHealth)
                    break
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "E3":
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
                        elif DamageAndCombatDoneList[2] == "Player"  and DamageAndCombatDoneList[1] != "Enemy Dead":
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
                        print("You have successfully defeated Enemy3! and gained 4 stat points because of it!")
                        PlayerStatPoints += 4
                        Space19 = "19"
                        break
                    elif DamageAndCombatDoneList[1] == "Player Dead":
                        print("You have sadly been defeated by Enemy3")
                        ThirdEnemyHealth = 12
                        PlayerDefeated = True
                if ThirdEnemyDefeated == True:
                    break
                elif PlayerDefeated == True:
                    PlayerDefeated = False
                    CurrentPlayerSpace = [0, 0]
                    PlayerHealth = int(PlayerStatHealth)
                    break
    elif GetMapSpace(CurrentPlayerSpace, GameMap) == "FB":
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
                        elif DamageAndCombatDoneList[2] == "Player"  and DamageAndCombatDoneList[1] != "Enemy Dead":
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
                        Space25 = "25"
                        break
                    elif DamageAndCombatDoneList[1] == "Player Dead":
                        print("You have sadly been defeated by The Final Boss.")
                        FinalBossHealth = 20
                        PlayerDefeated = True
                if FinalBossDefeated == True:
                    break
                elif PlayerDefeated == True:
                    PlayerDefeated = False
                    CurrentPlayerSpace = [0, 0]
                    PlayerHealth = int(PlayerStatHealth)
                    break