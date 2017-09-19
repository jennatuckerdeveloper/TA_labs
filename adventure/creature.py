"""
*   Creature
    * Location
    * Health
    * Weapon

"""

class Creature:
    def __init__(self, location="start", health=100, weapon=None):
        self.location = location
        self.health = health
        self.weapon = weapon
        self.inventory = []

    def take(self, item):
        self.inventory.append(item)
        print("Your inventory now includes: {}".format(item))

    def change_weapon(self, weapon):
        for item in self.inventory:
            if item.name == weapon:
                self.weapon = item

    def attack(self, creature):
        creature.health -= self.weapon.damage
        print("You attack with your {}.".format(self.weapon))
        print("Their health is now {}.".format(creature.health))

    def use_potion(self, potion):
        for item in self.inventory:
            if item.name == potion:
                self.health += item.potency
                self.inventory.remove(item) #This will work only if each potion is unique.
        print("Your health is now {}".format(self.health))
        self.see_inventory()

    def see_inventory(self):
        print("Your inventory now includes: ")
        for i in self.inventory:
            print(i.name)