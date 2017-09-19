import random

room_names = ['hall', 'hall', 'hall', 'lair', 'den']

class Characters:
    def __init__(self, name, attk, hp):
        self.name = name
        self.attk = attk
        self.hp = hp
        self.inv = []
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


    def fight(self, currentEnemy):
        currentEnemy.hp -= self.attk
        print('you hit enemy for {}'.format(self.attk))
        print(currentEnemy.hp)
        if currentEnemy.hp <= 0:
            print('enemy slain!')
            currentEnemy = None

class Items():
    def __init__(self, name, location, restore, val, spell):
        self.name = name
        self.location = location
        self.restore = restore
        self.val = val
        self.spell = spell

    def __str__(self):
        return self.name


class Weapons:
    def __init__(self, name, dmg):
        self.name = name
        # self.location = location
        self.dmg = dmg
        # self.val = val
        # self.durability = durability
        # self.ran_num = ran_num
    def __str__(self):
        return self.name

class Rooms:
    def __init__(self):
        # room_names = ['hall', 'hall', 'hall', 'lair', 'den']

        self.name = random.choice(room_names)
        room_names.remove(self.name)
        self.enemies = [enemies[random.randint(0, 1)]]
        self.items = items[random.randint(0, 1)]
        # print(room_names)
        # self.number = lastRoom + 1
        self.doors = {'north': 'n', 'south': 'n'}
        # print(self.doors)

        # print(lastRoom)
        # self.north
        # self.south
        # self.east
        # self.west

    def __str__(self):
        return self.name
        #
        # def room_gen(self):
        #     Rooms.name = random.choice(room_names)
        #     Rooms.enemies = enemies[randint(0,1)]


weapon = Weapons('sword', 10)

enemies = [Characters('orc', 20, 40),
           Characters('skeleton', 10, 30)]

weapons = [Weapons("sword", 20)]

items = [Items("Book", None, 0, 0, None),
         Items('potion', None, 10, 40, None)]

potions = [Items('potion', None, 10, 40, None)]


# print(weapon, weapon.dmg)

# rooms = [0, 1, 2]

player = Characters('Matt', 20, 60)


# enemies = [Characters('orc', 20, 40),
#            Characters('skeleton', 10, 30)]
#
#
# weapons = [Weapons("sword", 20)]
#
# books =[Items("Book", None, 0, 0, None)]
#
# potions = [Items('potion', None, 10, 40, None)]

# currentEnemy = enemies[randint(0, 1)]

def show_status():
    print('you are in the {}.'.format(playerLocation.name))
    if currentEnemy != None:
        print('you see a {}.'.format(currentEnemy))


# print(player, player.hp)
# print(weapons[0])
# player.hp = 80
# print(player.hp)


startRoom = Rooms()
currentEnemy = startRoom.enemies[0]
playerLocation = startRoom
# print(playerLocation)
#
# print(currentRoom.enemies[0])
# print(currentEnemy)


while True:

    show_status()
    print("Start of While:", playerLocation.doors)
    query = input("what??? ")
    if query in playerLocation.doors:
        if isinstance(playerLocation.doors[query], Rooms):
            print('running if statement')
            new_spot = playerLocation.doors[query]
            playerLocation = new_spot

        else:
            print('running else statement')
            print("Was entry pointing to Room?", isinstance(playerLocation.doors[query], Rooms))
            newRoom = Rooms()
            playerLocation.doors[query] = newRoom
            print("Current room doors", playerLocation.doors)
            reverse = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
            revQuery = reverse[query]

            newRoom.doors[revQuery] = playerLocation

            playerLocation = newRoom #Probably this line
            print("New room doors", playerLocation.doors)
            # print(currentRoom.enemies, currentRoom.name)
            # if isinstance(playerLocation.doors[query], Rooms):
            #     playerLocation = playeLocation.doors[query]


    # if query == 'fight':
    #     if currentEnemy in currentRoom.enemies:
    #         player.fight(currentEnemy)
    #         if currentEnemy.hp <= 0:
    #             currentRoom.enemies.remove(currentEnemy)
    #             currentEnemy = None