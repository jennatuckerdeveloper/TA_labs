from random import randint

"""
A simple dice game with a text-based interface merged into an app.
Five dice are rolled.  The user is allowed to re-roll or hold twice.
The round is scored.  A score is added to the user's points.  
Every round "costs" 10 points to play.  
User begins with 100 points.  Falling to 0 points ends the game.  
"""

class Interface:
    """
    A simple text-based interface for inputs and outputs.
    """
    def __init__(self):
        print("""Welcome to Luck of the Dice
You begin with 100 points.
Each round costs 10 to play.\n""")

    def display_dice(self, current_values):
        print("Dice show:", current_values, "\n")

    def which_to_roll(self):
        while True:
            try:
                choice = eval(input("Enter a list of which positions to roll ([] to stop rolling) "))
            except (NameError, SyntaxError) as error:
                continue
            if isinstance(choice, list) == True:
                return choice
            else:
                continue

    def show_luck(self, result, score, currency):
        print(result, score, currency)

    def close(self):
        print("Thanks for playing!")

class Dice_Game:
    """
    A dice game that holds five dice in a list.
    Methods to roll all dice, roll some dice, score dice, & return a copy of the dice list to display.
    """
    def __init__(self):
        self.dice = [0] * 5

    def roll_all(self):
        for die in range(0,5):
            self.dice[die] = randint(1,6)

    def roll_some(self, rolling): #rolling should be a list of the positions 1-5 of the die to roll
        for die in rolling:
            self.dice[int(die)-1] = randint(1,6)

    def score(self):
        matches = [0] * 7
        for side in self.dice:
            matches[side] += 1
        if 5 in matches:
            return "Five of a kind", 30
        elif 4 in matches:
            return "Four of a kind", 15
        elif (3 in matches) and (2 in matches):
            return "Full house", 12
        elif 3 in matches:
            return "Three of a kind", 8
        elif (2 not in matches) and (matches[1] == 0 or matches[6] == 0):
            return "Straight", 20
        elif matches.count(2) == 2:
            return "Two pairs", 5
        else:
            return "No luck", 0

    def show(self):
        return self.dice[:]

class Dice_App:

    """
    Brings together the Dice Game and Interface to run an ongoing game until end condition is met.
    """

    def __init__(self):
        self.dice = Dice_Game()
        self.interface = Interface()
        self.currency = 100

    def run(self):
        while self.currency > 0:
            self.playRound()
        self.interface.close()

    def playRound(self):
        self.currency -= 10
        self.run_rolls()
        result, score = self.dice.score()
        self.currency += score
        self.interface.show_luck(result, score, self.currency)

    def run_rolls(self):
        self.dice.roll_all()
        roll = 1
        self.interface.display_dice(self.dice.show())
        choose_rolls = self.interface.which_to_roll()
        while roll < 3 and choose_rolls != []:
            self.dice.roll_some(choose_rolls)
            roll += 1
            self.interface.display_dice(self.dice.show())
            if roll < 3:
                choose_rolls = self.interface.which_to_roll()

my_game = Dice_App()
my_game.run()