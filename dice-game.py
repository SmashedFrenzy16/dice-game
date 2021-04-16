import random
import string
import time

game_start = input("Would you like to roll the dice? \n")

def dice_roll():
    time.sleep(1)
    print('''Please wait while the computer rolls your dice.
At peak times this can take a few moments...\n''')
    time.sleep(5)
    print("Your number is: " + str(random.randint(1,6)))
    global play_again
    play_again = input("Would you like to play again? ")

if game_start == "yes" or game_start == "Yes" or game_start == "y" or game_start == "Y":
    dice_roll()
    while play_again == "yes" or play_again == "Yes" or play_again == "y" or play_again == "Y":
        dice_roll()
elif game_start == "no" or game_start == "No" or game_start == "n" or game_start == "N":
    print("Goodbye!")
else:
    print("Sorry, we could not recognize your input.")
