#Max Holdaway Fix The Game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    #Having attempts be 0 caused the user to have 11 attempts instead of 10 this is a logic error
    attempts = 1
    game_over = False
    while not game_over:
        #The input for guess needs to be inside an int function this is a logic error it made it so that the code couldn't compare the users answer to the number being guessed
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        #Changing this to an elif made it so that the too low or too high messsage doesn't appear anymore when you have used all your attempts up this is a logic error
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            #Without the addition to attempts the user could guess forever this is a logic error
            attempts += 1
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            #Without the addition to attempts the user could guess forever this is a logic error
            attempts += 1
        continue
    print("Game Over. Thanks for playing!")
start_game()