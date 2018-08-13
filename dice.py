import time
import random
def roll_dice():
    dice_decision = input("would you like to roll the dice?")
    if dice_decision == "yes":
        print("rolling the dice... ")
        time.sleep(3)
        dice_number = random.randint(1,6)
        print(dice_number)
        return dice_number
    else:
        print("come back when you want to roll!")
