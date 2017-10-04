from random import randint

def dice_game():
    num_dice = int(input("How many dice do you want to roll? "))
    num_side = int(input("How many sides should each die have? "))
    while num_dice > 0:
        dice_roll = randint(1, num_side)
        print(dice_roll)
        num_dice -= 1

dice_game()

