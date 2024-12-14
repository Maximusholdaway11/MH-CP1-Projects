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

DamageAndCombatDoneList = []

PlayerStatPoints = 0

PlayerHasDoneCombat = False

PlayerHasDefended = False

PlayerStartingHealth = 5

EuippedItem = "Stick"

ItemBelt = ["Stick"]

PlayerStatHealth = 1

PlayerHealth = PlayerStartingHealth + PlayerStatHealth

PlayerStatAttack = 1

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
    PlayerHasDoneCombatFVar == False
    if EnemyHealthFVar == 0:
        EnemyDefeated = "Enemy Dead"
    elif PlayerHealthFVar == 0:
        PlayerDefeated = "Player Dead"
    if EnemyDefeated == "Enemy Dead":
        PlayerHasDoneCombatFVar = True
        DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
        DamageAndCombatDoneListFVar.append(EnemyDefeated)
        return DamageAndCombatDoneListFVar
    elif PlayerDefeated == "Player Dead":
        PlayerHasDoneCombatFVar = True
        DamageAndCombatDoneListFVar.append(PlayerHasDoneCombatFVar)
        DamageAndCombatDoneListFVar.append(PlayerDefeated)
        return DamageAndCombatDoneListFVar
    elif EnemyDefeated != "Enemy Dead" and PlayerDefeated != "Player Dead":
        PlayerCombatDecision = str(input(f"Do you want to Attack, Defend, or Run Away? Also Your health is at {PlayerHealthFVar} The enemy's health is at {EnemyHealthFVar}"))
        DamageAndCombatDoneListFVar = []
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

