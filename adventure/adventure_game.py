"""# Practice: Adventure Game

Save your solution in a directory in `practice/` named `adventure`.

Write a [NetHack](https://en.wikipedia.org/wiki/NetHack)-like terminal based dungeon crawler game.

There are various **entities** in the game.
Make each entity a class in it's own module.

*   Creature
    * Location
    * Health
    * Weapon

*   Weapon
    * Location (or None if picked up)
    * Damage

*   Potion
    * Location
    * Health Restored

Put any functions that manipulate these classes in their respective modules.

"""
from potion import Potion
from weapon import Weapon
from creature import Creature

rooms = ["start", "kitchen", "dining", "pantry"]

player = Creature()

creatures = [Creature("kitchen")]

weapons = [ Weapon('dagger', 'kitchen', 20),
            Weapon('sword', 'dining', 30),
            Weapon('axe','pantry', 40)
          ]
potions = [ Potion('red', 'kitchen', 20),
            Potion('blue', 'dining', 30),
            Potion('green', 'pantry', 40)
        ]



def game():

    while True:
        play = input(  """
                Do you want to:
                1) Go to the next room.
                2) Pick up weapon.
                3) Change weapon in use.
                4) Pick up potion.
                5) Attack! 
                6) Use healing potion. 
                7) Quit
                """
              )
        if play == "1":
            player.location = rooms[rooms.index(player.location) + 1]

            print("Room: {}".format(player.location))

            for weapon in weapons:
                if player.location == weapon.location:
                    print("There is a {}".format(weapon.name))

            for potion in potions:
                if player.location == potion.location:
                    print("There is a {} potion".format(potion.name))

        if play == "2":
            for weapon in weapons:
                if weapon.location == player.location:
                    player.take(weapon)
                    weapon.location = None

        if play == "3":
            player.see_inventory()
            choice = input("Which weapon do you want to use? ")
            player.change_weapon(choice)
            print("You are now carrying: {}".format(player.weapon))

        if play == "4":
            for potion in potions:
                if potion.location == player.location:
                    player.take(potion)
                    potion.location = None

        if play == "5":
            for creature in creatures:
                if creature.location == player.location:
                    player.attack(creature)

        if play == "6":
            print("Your health is {}".format(player.health))
            player.see_inventory()
            choice = input("Which potion do you want to use? ")
            player.use_potion(choice)

        if play == "7":
            quit()

game()
