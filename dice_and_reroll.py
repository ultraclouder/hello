import dice
import random
import time

def ultimatedie():
    dice_number = dice.roll_dice()
    while (dice_number == 6) or (dice_number == 5):
        dice_number = dice.roll_dice()
    