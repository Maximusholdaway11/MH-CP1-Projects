#Max Holdaway Final Project

print("This is my adventure game, have a good time!")

print("For movement simply choose a blank that you are right next to. Also walls will block you when trying to move.")

import random as random

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

Space17 = "Enemy3"

Space18 = "Space18"

Space19 = "Enemy2"

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

PlayerStartingHealth = 5

EquippedItem = "Stick"

ItemBelt = ["Stick"]

PlayerStatHealth = 1

PlayerStatDamage = 1

PlayerStatDefense = 1

FirstEnemyHealth = 5

FirstEnemyDamage = 3

FirstEnemyDefense = 2

FirstEnemyDefeated = False

SecondEnemyHealth = 5

SecondEnemyDamage = 3

SecondEnemyDefense = 2

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
    elif CurrentPlayerSpace == "Enemy1":
        if SpacePlayerIsMovingTo == "Exit/Start":
            CurrentPlayerSpace = "Exit/Start"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space6":
            CurrentPlayerSpace = "Space6"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Space3":
            CurrentPlayerSpace = "Space3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space8":
            CurrentPlayerSpace = "Space8"
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
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space8":
            CurrentPlayerSpace = "Space8"
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
        elif SpacePlayerIsMovingTo == "Space8":
            CurrentPlayerSpace = "Space8"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space10":
            CurrentPlayerSpace = "Space10"
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
    elif CurrentPlayerSpace == "Space6":
        if SpacePlayerIsMovingTo == "Exit/Start":
            CurrentPlayerSpace = "Exit/Start"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy1":
            CurrentPlayerSpace = "Enemy1"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Space11":
            CurrentPlayerSpace = "Space11"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
    elif CurrentPlayerSpace == "Space8":
        if SpacePlayerIsMovingTo == "Space4":
            CurrentPlayerSpace = "Space4"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
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
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
    elif CurrentPlayerSpace == "Space10":
        if SpacePlayerIsMovingTo == "Chest4":
            CurrentPlayerSpace = "Chest4"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Chest3":
            CurrentPlayerSpace = "Chest3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space4":
            CurrentPlayerSpace = "Space4"
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space11":
        if SpacePlayerIsMovingTo == "Space6":
            CurrentPlayerSpace = "Space6"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space16":
            CurrentPlayerSpace = "Space16"
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Chest5":
        if SpacePlayerIsMovingTo == "Space8":
            CurrentPlayerSpace = "Space8"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall4":
            print("Can't move there it's a wall.")
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
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
    elif CurrentPlayerSpace == "Chest3":
        if SpacePlayerIsMovingTo == "Space10":
            CurrentPlayerSpace = "Space10"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall1":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space20":
            CurrentPlayerSpace = "Space20"
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space16":
        if SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall5":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Space11":
            CurrentPlayerSpace = "Space11"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest1":
            CurrentPlayerSpace = "Chest1"
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Enemy2":
        if SpacePlayerIsMovingTo == "Chest5":
            CurrentPlayerSpace = "Chest5"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall5":
            print("Can't move there it's a wall.")
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
    elif CurrentPlayerSpace == "Space18":
        if SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest5":
            CurrentPlayerSpace = "Chest5"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall3":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Chest2":
            CurrentPlayerSpace = "Chest2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall6":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall5":
            print("Can't move there it's a wall.")
    elif CurrentPlayerSpace == "Enemy3":
        if SpacePlayerIsMovingTo == "Space18":
            CurrentPlayerSpace = "Space18"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall3":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "FinalBoss":
            CurrentPlayerSpace = "FinalBoss"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest2":
            CurrentPlayerSpace = "Chest2"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest3":
            CurrentPlayerSpace = "Chest3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Space20":
            CurrentPlayerSpace = "Space20"
            return CurrentPlayerSpace
    elif CurrentPlayerSpace == "Space20":
        if SpacePlayerIsMovingTo == "FinalBoss":
            CurrentPlayerSpace = "FinalBoss"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall2":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall3":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Chest3":
            CurrentPlayerSpace = "Chest3"
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
    elif CurrentPlayerSpace == "Chest2":
        if SpacePlayerIsMovingTo == "Space18":
            CurrentPlayerSpace = "Space18"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Wall5":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Wall3":
            print("Can't move there it's a wall.")
        elif SpacePlayerIsMovingTo == "Enemy3":
            CurrentPlayerSpace = "Enemy3"
            return CurrentPlayerSpace
        elif SpacePlayerIsMovingTo == "Enemy2":
            CurrentPlayerSpace = "Enemy2"
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
    else:
        print("Unexpected Error Has Occurred Please Try Again")

def Combat(EnemyHealthFVar, PlayerHealthFVar, EnemyDamageFVar, PlayerDamageFVar, EnemyDefenseFVar, PlayerDefenseFVar):
    DamageAndCombatDoneListFVar = []
    PlayerHasDoneCombatFVar == False
    if EnemyHealthFVar == 0:
        EnemyDefeatedFVar = "Enemy Dead"
    elif PlayerHealthFVar == 0:
        PlayerDefeatedFVar = "Player Dead"
    if EnemyDefeatedFVar == "Enemy Dead":
        PlayerHasDoneCombatFVar = True
        DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
        DamageAndCombatDoneListFVar.append(EnemyDefeatedFVar)
        return DamageAndCombatDoneListFVar
    elif PlayerDefeatedFVar == "Player Dead":
        PlayerHasDoneCombatFVar = True
        DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
        DamageAndCombatDoneListFVar.append(PlayerDefeatedFVar)
        return DamageAndCombatDoneListFVar
    elif EnemyDefeatedFVar != "Enemy Dead" and PlayerDefeatedFVar != "Player Dead":
        PlayerCombatDecision = str(input(f"Do you want to Attack, Defend, or Run Away? Also Your health is at {PlayerHealthFVar} The enemy's health is at {EnemyHealthFVar}"))
        PlayerHasDoneCombatFVar = False
        PlayerHasDefendedFVar = False
        if PlayerCombatDecision == "Attack":
            EnemyDecision = random.randint(1, 5)
            if EnemyDecision >= 4:
                EnemyDodgedAttack = random.randint(1, 10)
                if EnemyDodgedAttack >= 3:
                    print("The enemy dodged the attack!")
                    PlayerHasDoneCombatFVar = True
                    DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
                    return DamageAndCombatDoneListFVar
                elif EnemyDodgedAttack <= 2:
                    EnemyDamageReduction = PlayerDamageFVar - EnemyDefenseFVar
                    EnemyHealthFVar -= EnemyDamageReduction
                    print(f"The enemy has defended but you have still hit the enemy for {EnemyDamageReduction} damage and the enemy now has {EnemyHealthFVar} health!")
                    PlayerHasDoneCombatFVar = True
                    DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
                    DamageAndCombatDoneListFVar.append(EnemyHealthFVar)
                    DamageAndCombatDoneListFVar.append("Enemy")
                    return DamageAndCombatDoneListFVar
            elif EnemyDecision <= 2:
                EnemyHealthFVar -= PlayerDamageFVar
                print(f"You have hit the enemy for {PlayerDamageFVar} damage and the enemy now has {EnemyHealthFVar} health!")
                PlayerHealthFVar -= EnemyDamageFVar
                print(f"The enemy has hit you for {EnemyDamageFVar} damage and you now have {PlayerHealthFVar} health.")
                PlayerHasDoneCombatFVar = True
                DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
                DamageAndCombatDoneListFVar.append(EnemyHealthFVar)
                DamageAndCombatDoneListFVar.append(PlayerHealthFVar)
                DamageAndCombatDoneListFVar.append("Both")
                return DamageAndCombatDoneListFVar
            elif EnemyDecision == 3:
                EnemyWasAbleToRunAwayFVar = random.randint(1, 2)
                if EnemyWasAbleToRunAwayFVar == 1:
                    EnemyHealthFVar -= PlayerDamageFVar
                    print(f"You have hit the enemy for {PlayerDamageFVar} damage and the enemy now has {EnemyHealthFVar} health!")
                    PlayerHasDoneCombatFVar = True
                    DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
                    DamageAndCombatDoneListFVar.append(EnemyHealthFVar)
                    DamageAndCombatDoneListFVar.append("Enemy")
                    return DamageAndCombatDoneListFVar
                elif EnemyWasAbleToRunAwayFVar == 2:
                    print("The enemy was able to run away.")
                    PlayerHasDoneCombatFVar = True
                    DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
                    return DamageAndCombatDoneListFVar
            else:
                print("An unexpected error has occurred please try again")
        elif PlayerCombatDecision == "Defense":
            PlayerDodgedAttack = random.randint(1, 10)
            if PlayerDodgedAttack >= 3:
                PlayerDamageReduction = EnemyDamageFVar - PlayerDefenseFVar
                PlayerHealthFVar -= PlayerDamageReduction
                print(f"You have successfully defended and the enemy only did {PlayerDamageReduction} damage! and you now have {PlayerHealthFVar} health.")
                PlayerHasDefendedFVar = True
                DamageAndCombatDoneListFVar.append(PlayerHasDefendedFVar)
                DamageAndCombatDoneListFVar.append(PlayerHealthFVar)
                DamageAndCombatDoneListFVar.append("Player")
                return DamageAndCombatDoneListFVar
            elif PlayerDodgedAttack <= 2:
                print("You dodged their attack!")
                PlayerHasDefendedFVar = True
                DamageAndCombatDoneListFVar.append(PlayerHasDefendedFVar)
                return DamageAndCombatDoneListFVar
        elif PlayerCombatDecision == "Run Awway":
            PlayerWasAbleToRunAway = random.randint(1, 2)
            if PlayerWasAbleToRunAway == 1:
                if EnemyDecision <= 2:
                    PlayerHealthFVar -= EnemyDamageFVar
                    print(f"You have failed to run away and the enemy has hit you for {EnemyDamageFVar} damage. and you now have {PlayerHealthFVar} health.")
                    PlayerHasDoneCombatFVar = True
                    DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
                    DamageAndCombatDoneListFVar.append(PlayerHealthFVar)
                    DamageAndCombatDoneListFVar.append("Player")
                    return DamageAndCombatDoneListFVar
            elif PlayerWasAbleToRunAway == 2:
                print("You have successfully run away!")
                PlayerHasDoneCombatFVar = True
                DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
                DamageAndCombatDoneListFVar.append(EnemyHealthFVar)
                DamageAndCombatDoneListFVar.append(PlayerHealthFVar)
                DamageAndCombatDoneListFVar.append("Both")
                return DamageAndCombatDoneListFVar

def FinalBossCombat(EnemyHealthFVar2, PlayerHealthFVar2, EnemyDamageFVar2, PlayerDamageFVar2, EnemyDefenseFVar2, PlayerDefenseFVar2):
    DamageAndCombatDoneListFVar2 = []
    PlayerHasDoneCombatFVar2 == False
    if EnemyHealthFVar2 == 0:
        FinalBossDefeatedFVar = "Enemy Dead"
    elif PlayerHealthFVar2 == 0:
        PlayerDefeatedFVar2 = "Player Dead"
    if FinalBossDefeatedFVar == "Enemy Dead":
        PlayerHasDoneCombatFVar2 = True
        DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
        DamageAndCombatDoneListFVar2.append(FinalBossDefeatedFVar)
        return DamageAndCombatDoneListFVar2
    elif PlayerDefeatedFVar2 == "Player Dead":
        PlayerHasDoneCombatFVar2 = True
        DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
        DamageAndCombatDoneListFVar2.append(PlayerDefeatedFVar2)
        return DamageAndCombatDoneListFVar2
    elif FinalBossDefeatedFVar != "Enemy Dead" and PlayerDefeatedFVar2 != "Player Dead":
        PlayerCombatDecision = str(input(f"Do you want to Attack, Defend, or Run Away? Also Your health is at {PlayerHealthFVar2} The enemy's health is at {EnemyHealthFVar2}"))
        PlayerHasDoneCombatFVar2 = False
        PlayerHasDefendedFVar2 = False
        if PlayerCombatDecision == "Attack":
            FinalBossDecision = random.randint(1, 5)
            if FinalBossDecision <= 2:
                FinalBossDodgedAttack = random.randint(1, 10)
                if FinalBossDodgedAttack >= 3:
                    print("The enemy dodged the attack!")
                    PlayerHasDoneCombatFVar2 = True
                    DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
                    return DamageAndCombatDoneListFVar2
                elif FinalBossDodgedAttack <= 2:
                    EnemyDamageReductionFVar = PlayerDamageFVar2 - EnemyDefenseFVar2
                    EnemyHealthFVar2 -= EnemyDamageReductionFVar
                    print(f"The enemy has defended but you have still hit the enemy for {EnemyDamageReductionFVar} damage and the enemy now has {EnemyHealthFVar2} health!")
                    PlayerHasDoneCombatFVar2 = True
                    DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar)
                    DamageAndCombatDoneListFVar2.append(EnemyHealthFVar2)
                    DamageAndCombatDoneListFVar2.append("Enemy")
                    return DamageAndCombatDoneListFVar2
            elif FinalBossDecision >= 3:
                EnemyHealthFVar2 -= PlayerDamageFVar2
                print(f"You have hit the enemy for {PlayerDamageFVar2} damage and the enemy now has {EnemyHealthFVar2} health!")
                PlayerHealthFVar2 -= EnemyDamageFVar2
                print(f"The enemy has hit you for {EnemyDamageFVar2} damage and you now have {PlayerHealthFVar2} health.")
                PlayerHasDoneCombatFVar = True
                DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar)
                DamageAndCombatDoneListFVar2.append(EnemyHealthFVar2)
                DamageAndCombatDoneListFVar2.append(PlayerHealthFVar2)
                DamageAndCombatDoneListFVar2.append("Both")
                return DamageAndCombatDoneListFVar2
        elif PlayerCombatDecision == "Defense":
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
        elif PlayerCombatDecision == "Run Awway":
            PlayerWasAbleToRunAway = random.randint(1, 2)
            if PlayerWasAbleToRunAway == 1:
                if EnemyDecision <= 2:
                    PlayerHealthFVar2 -= EnemyDamageFVar2
                    print(f"You have failed to run away and the enemy has hit you for {EnemyDamageFVar2} damage. and you now have {PlayerHealthFVar2} health.")
                    PlayerHasDoneCombatFVar2 = True
                    DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
                    DamageAndCombatDoneListFVar2.append(PlayerHealthFVar2)
                    DamageAndCombatDoneListFVar2.append("Player")
                    return DamageAndCombatDoneListFVar2
            elif PlayerWasAbleToRunAway == 2:
                print("You have successfully run away!")
                PlayerHasDoneCombatFVar2 = True
                DamageAndCombatDoneListFVar2.append(PlayerHasDoneCombatFVar2)
                DamageAndCombatDoneListFVar2.append(EnemyHealthFVar2)
                DamageAndCombatDoneListFVar2.append(PlayerHealthFVar2)
                DamageAndCombatDoneListFVar2.append("Both")
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
            print("You have found the first chest inside it gives you three stat points!")
            PointAmountGiven = 3
            ChestFVarList = [PointAmountGiven, True]
            return ChestFVarList
        elif ChestOpened == True:
            pass
    if CurrentPlayerSpaceFVar == "Chest4":
        if ChestOpened == False:
            print("You have found the first chest inside it gives you four stat points!")
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

CurrentPlayerSpace = "Exit/Start"

PlayerKeyHolder = ""

FirstChestOpened = False

SecondChestOpened = False

ThirdChestOpened = False

FourthChestOpened = False

FifthChestOpened = False

for x in GameMap:
    print(x)

print(f"You have been started at {CurrentPlayerSpace}!")

while True:
    if EquippedItem == "Stick":
        WeaponStatDamage = 1
    elif EquippedItem == "Sword":
        WeaponStatDamage = 4

    DamageAndCombatDoneList = []
    PlayerDamage = PlayerStatDamage + WeaponStatDamage
    PlayerHealth = PlayerStartingHealth + PlayerStatHealth
    PlayerDefense = PlayerStatDefense

    for x in GameMap:
        print(x)

    if PlayerKeyHolder == "Key" and CurrentPlayerSpace == "Exit/Start":
        print("You have won the game congrats!")
        break

    if CurrentPlayerSpace == "Chest1":
        ChestList1 = ChestOpener(CurrentPlayerSpace, FirstChestOpened)
        if FirstChestOpened == False:
            PlayerStatPoints += ChestList1[0]
            FirstChestOpened = ChestList1[1]
        elif FirstChestOpened == True:
            pass
    elif CurrentPlayerSpace == "Chest2":
        ChestList2 = ChestOpener(CurrentPlayerSpace, SecondChestOpened)
        if SecondChestOpened == False:
            PlayerStatPoints += ChestList2[0]
            SecondChestOpened = ChestList2[1]
        if SecondChestOpened == True:
            pass
    elif CurrentPlayerSpace == "Chest3":
        ChestList3 = ChestOpener(CurrentPlayerSpace, ThirdChestOpened)
        if ThirdChestOpened == False:
            PlayerStatPoints += ChestList3[0]
            ThirdChestOpened = ChestList3[1]
        if ThirdChestOpened == True:
            pass
    elif CurrentPlayerSpace == "Chest4":
        ChestList4 = ChestOpener(CurrentPlayerSpace, FourthChestOpened)
        if FourthChestOpened == False:
            PlayerStatPoints += ChestList4[0]
            FourthChestOpened = ChestList4[1]
        if FourthChestOpened == True:
            pass
    elif CurrentPlayerSpace == "Chest5":
        ChestList5 = ChestOpener(CurrentPlayerSpace, FifthChestOpened)
        if FifthChestOpened == False:
            ItemBelt.append(ChestList5[0])
            FifthChestOpened = ChestList5[1]
        if FifthChestOpened == True:
            pass
    
    PlayerDecision = str(input("Do you want to move, check your inventory or check / use your stats?? (Type Move for movement, Inventory for inventory checking, and Stats for Stats checking / using them): "))

    if PlayerDecision == "Move":
        SpacePlayerIsMovingTo = str(input("Which space do you want to move to?: "))
        CurrentPlayerSpace = Movement(SpacePlayerIsMovingTo, CurrentPlayerSpace)
        print(f"You have moved to {CurrentPlayerSpace}!")
    elif PlayerDecision == "Inventory":
        while True:
            PlayerInventoryAction = str(input("Do you want to swap the item you currently have, Exit your inventory, or Put away an item? (Say Swap to swap your stick and the item you will get, Store to store an item, and Exit to exit the inventory (You need to store items to swap them or you can just store the stick and it will swap to the other item)): "))
            if PlayerInventoryAction == "Swap":
                if InventoryList != []:
                    PlayerSwapAction = str(input("What item do you want to swap?: "))
                    print(InventoryList)
                    if PlayerSwapAction == "Sword":
                        if EquippedItem == "Sword":
                            print("You can't swap out your sword for your sword.")
                            continue
                        elif EquippedItem == "Stick":
                            EquippedItem == "Sword"
                            InventoryList.remove("Sword")
                            InventoryList.append("Stick")
                            print("You have succesfully swapped out your stick for your sword!")
                        elif EquippedItem == "Nothing":
                            print("You can't swap out nothing for a sword!")
                            continue
                        else:
                            print("Unexpected error try again.")
                            continue
                    elif PlayerSwapAction == "Stick":
                        if EquippedItem == "Stick":
                            print("You can't swap out your stick for your stick.")
                            continue
                        elif EquippedItem == "Sword":
                            EquippedItem == "Stick"
                            InventoryList.remove("Stick")
                            InventoryList.append("Sword")
                            print("You have succesfully swapped out your sword for your stick!")
                        elif EquippedItem == "Nothing":
                            print("You can't swap out nothing for a stick!")
                            continue
                        else:
                            print("Unexpected error try again.")
                            continue
                elif InventoryList == []:
                    print("You can't swap anything you don't have anything in your inventory.")
                    continue
            elif PlayerInventoryAction == "Store":
                if len(ItemBelt) == 2:
                    PlayerStoreAction = str(input("What do you want to store?: "))
                    if PlayerStoreAction == "Sword":
                        if EquippedItem in ["Stick"]:
                            if InventoryList not in ["Sword"]:
                                ItemBelt.remove("Sword")
                                InventoryList.append("Sword")
                                print("You have successfully added your sword to your inventory!")
                            elif InventoryList in ["Sword"]:
                                print("You can't store your sword it's already in your inventory.")
                        elif EquippedItem in ["Sword"]:
                            ItemBelt.remove("Sword")
                            InventoryList.append("Sword")
                            EquippedItem = "Nothing"
                            if InventoryList in ["Stick", "Sword"]:
                                InventoryList.remove("Stick")
                                ItemBelt.append("Stick")
                                EquippedItem = "Stick"
                                print("You have succesfully added your sword to your inventory and equipped your stick!")
                            elif ItemBelt in ["Stick"]:
                                EquippedItem = "Stick"
                                print("You have succesfully added your sword to your inventory and equipped your stick!")
                        elif EquippedItem in ["Nothing"]:
                            print("You can't store nothing.")
                            continue
                    elif PlayerStoreAction == "Stick":
                        if EquippedItem in ["Sword"]:
                            if InventoryList not in ["Stick"]:
                                ItemBelt.remove("Stick")
                                InventoryList.append("Stick")
                                print("You have successfully added your stick to your inventory!")
                            elif InventoryList in ["Sword"]:
                                print("You can't store your stick it's already in your inventory.")
                        elif EquippedItem in ["Stick"]:
                            ItemBelt.remove("Stick")
                            InventoryList.append("Stick")
                            EquippedItem = "Nothing"
                            if InventoryList in ["Sword", "Stick"]:
                                InventoryList.remove("Sword")
                                ItemBelt.append("Sword")
                                EquippedItem = "Sword"
                                print("You have succesfully added your stick to your inventory and equipped your sword!")
                            elif ItemBelt in ["Sword"]:
                                EquippedItem = "Sword"
                                print("You have succesfully added your stick to your inventory and equipped your sword!")
                        elif EquippedItem in ["Nothing"]:
                            print("You can't store nothing.")
                            continue
                elif len(ItemBelt) == 1:
                    print("You can't store anything you don't have anything other than your stick to store!")
                    continue
            elif PlayerInventoryAction == "Exit":
                print("Hope you had a succesfull inventory use!")
                break
    elif PlayerDecision == "Stats":
        while True:
            PlayerStatAction = str(input("Do you want to check your stats, use your stat points, or exit your stats? (To check stats type Stats, to use stat points type Points, to exit type Exit)"))
            if PlayerStatAction == "Stats":
                print(f"These are your current stats Health is {PlayerStatHealth}, Damage is {PlayerStatDamage}, and Defense is {PlayerStatDefense}.")
            elif PlayerStatAction == "Points":
                if PlayerStatPoints > 0:
                    while True:
                        PlayerStatDecision = str(input(f"What stat do you want to add to? Also you currently have This many stat points {PlayerStatPoints}. (Type Damage for damage, Health for health, and Defense for defense)"))
                        if PlayerStatDecision == "Damage":
                            print("How much do you want to add to Damage?")
                            DamagePointAdd = int(input("Number: "))
                            if DamagePointAdd > PlayerStatPoints:
                                print("You can't add more points than you have! Please Decide the number of points you want to add again.")
                                DamagePointAdd = int(input("Number: "))
                                PlayerStatDamage += DamagePointAdd
                                print(f"You have successfully added {DamagePointAdd} points to damage!")
                                DamagePointAdd = 0
                            elif DamagePointAdd <= PlayerStatPoints:
                                PlayerStatDamage += DamagePointAdd
                                print(f"You have successfully added {DamagePointAdd} points to damage!")
                                DamagePointAdd = 0
                        if PlayerStatDecision == "Health":
                            print("How much do you want to add to Health?")
                            HealthPointAdd = int(input("Number: "))
                            if HealthPointAdd > PlayerStatPoints:
                                print("You can't add more points than you have! Please Decide the number of points you want to add again.")
                                HealthPointAdd = int(input("Number: "))
                                PlayerStatHealth += HealthPointAdd
                                print(f"You have successfully added {HealthPointAdd} points to health!")
                                HealthPointAdd = 0
                            elif HealthPointAdd <= PlayerStatPoints:
                                PlayerStatHealth += HealthPointAdd
                                print(f"You have successfully added {HealthPointAdd} points to health!")
                                HealthPointAdd = 0
                        if PlayerStatDecision == "Defense":
                            print("How much do you want to add to Defense?")
                            DefensePointAdd = int(input("Number: "))
                            if DefensePointAdd > PlayerStatPoints:
                                print("You can't add more points than you have! Please Decide the number of points you want to add again.")
                                DefensePointAdd = int(input("Number: "))
                                PlayerStatDefense += DefensePointAdd
                                print(f"You have successfully added {DefensePointAdd} points to defense!")
                                DefensePointAdd = 0
                            elif DefensePointAdd <= PlayerStatPoints:
                                PlayerStatDefense += DefensePointAdd
                                print(f"You have successfully added {DefensePointAdd} points to defense!")
                                DefensePointAdd = 0
                        elif PlayerStatDecision == "Exit":
                            print("Hope you had a succesful time using stats!")
                            break