import random
import os
# Introduction
end_of_game = False

def clear ():
    clear = lambda: os.system('clear') 
    clear()
    
def play_again():
    global end_of_game
    play_again = input("Play again? ('Y' for yes, 'N' for No: )")
    if play_again.lower() == "y":
            clear()
            play_game()
            
    elif play_again.lower() == "n":
        end_of_game = True


def play_game():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    random_number = random.randint(1,101)
    print(f"shh, the random number is {random_number}")

    difficulty = input("choose your difficulty, Easy or Hard: ")
    if difficulty.lower() == "easy":
        lives = 10
        print(f"You have {lives} chances to guess the number.")
        
    elif difficulty.lower() == "hard":
        lives = 5
        print(f"You have {lives} chances to guess the number.")

    def check_game_over():
        global end_of_game
        if lives == 0:
            print("Sorry, you lost. ")
            print(f"The number was {random_number}.")
            play_again()
            end_of_game = True


    while not end_of_game:
        guess = int(input("Guess a number: "))
        
        if guess != random_number and guess > random_number:
            clear()
            print("Too high")
            print("Guess again")
            lives -= 1
            check_game_over()
            
        elif guess != random_number and guess < random_number:
            clear()
            print("Too low")
            print("Guess again")
            lives -= 1
            print(f"You have {lives} guess left")
            check_game_over()
            
        elif guess == random_number:
            print(f"Congrats, the number was {random_number}, you win!")
            play_again()
            break


play_game()
        
        



# gueses the number 

# if wrong
# tell the user if too high or too low
# minus a life 
# guess again
# this is a loop?

# if easy level then 10 attempts
# # if wrong
# # tell the user if too high or too low
# # minus a life 
# # guess again
# # this is a loop?

# note that the rules of the guess will be lopped as a functiuon i think 