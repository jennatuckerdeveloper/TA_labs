import random


class Character:
    def __init__(self, location):
        self.location = location #Creates a character with a location.


class Enemy:
    def __init__(self):
        names = ['an ogre', 'a human', 'a troll']
        self.name = random.choice(names)
        attack_power = [20, 30, 40]
        self.attack = random.choice(attack_power)

    def __str__(self):
        return "{}".format(self.name)


class Item:
    def __init__(self):
        names = ['a potion.', 'a scroll.', 'a bottle.']
        self.name = random.choice(names)
        potency_levels = [20, 30, 40]
        self.potency = random.choice(potency_levels)

    def __str__(self):
        return "{}".format(self.name)


class Doors:

    def __init__(self):
        self.doorways = self.make_room_doors()

    def make_room_doors(self):
        cardinals = ['north', 'south', 'east', 'west'] #Keys for my doors dictionary.
        num_doors = random.randint(4, 4)  #Random number of doors in a new Room.
        this_room_doors = [] #This unique rooms list of doors.
        while num_doors > 0: #While loop creates this unique rooms list of doors.
            each = random.choice(cardinals)
            cardinals.remove(each)
            this_room_doors.append(each)
            num_doors -= 1
        return this_room_doors


class Inventory:
    def __init__(self):
        self.inventory = []

    def room_enemies(self):
        num_enemies = random.randint(0, 1)
        while num_enemies > 0:
            an_enemy = Enemy()
            self.inventory.append(an_enemy)
            num_enemies -= 1

    def room_items(self):
        num_items = random.randint(1, 2)
        while num_items > 0:
            an_item = Item()
            self.inventory.append(an_item)
            num_items -= 1


class Room:

    def __init__(self, coordinates=None, name=None, enemies=None): #These default to None, so they will initiate.  I can manually enter or randomly genderate replacement values below.
        self.coordinates = coordinates  # The coordinates mainly works to check to see if the map is working properly.

        self.name = name
        self.enemies = Inventory()
        self.items = Inventory()

        self.doorways = Doors()
        self.memory = {}  # This will become doors in the four cardinal directions.
        for door in self.doorways.doorways: #Fills this Rooms doors dictionary with cardinal keys and values of empty strings or unknowns to be replaced with rooms.
            self.memory[door] = ""

        self.fill_rooms()
        
    def fill_rooms(self):
        if self.coordinates != (0,0):
            self.name_room()
            self.enemies.room_enemies()
            self.items.room_items()

    def name_room(self):
        rooms = ['a hallway', 'a chamber', 'a storeroom']
        self.name = random.choice(rooms)

    def see_room(self):

        """
        The see_room method prints the player's room doors, enemies, and items the console for the user.
        """

        print("You are in", self.name, self.coordinates)
        for enemy in self.enemies.inventory:
            print("You see", enemy)
        for item in self.items.inventory:
            print("You see", item)
        print("There are doors that lead: ")
        for key in self.memory.keys():
            print(key)


class Game:
    def __init__(self):

        """
        The __init__ method for Game:
            1. creates an empty dictionary called self.map to record each room.
            2. creates a Room for the start location named "an entryway" at coordinates (0,0)
            3. creates a player character at the start location.
            4. records the start location's unique coordinates to the map record of rooms.

        """

        self.map = {} #Should this map of all Rooms be a class itself?  Why?  Why not?  
        self.start = Room((0, 0), "an entryway")  # Instantiates first room.
        self.player = Character(self.start)  # Instantiates player character.
        self.map[self.start.coordinates] = self.start #Enters first room into game map of all existing rooms.

    def map_room(self, head):

        """
        The map_room method takes the direction of the move the user wants to make and determines both the coordinates
        of the room the user wants to enter and the reverse direction of the user's choice of which way to move.
        """

        coordinates_change = {'north': (0, 1), 'south': (0, -1), 'east': (1, 0), 'west': (-1, 0)}
        new_coordinates = ((self.player.location.coordinates[0] + coordinates_change[head][0]),
                        (self.player.location.coordinates[1] + coordinates_change[head][1]))
        reverse = {'north': 'south', 'south': 'north', 'east': 'west',
                   'west': 'east'}  # Reverse directions.
        record = reverse[head]  # The reverse direction of what the user chose for the move.

        return new_coordinates, record

    def return_to_room(self, new_coordinates, record, head):

        """
        The return_to_room method runs when the player makes a move to re-enter an already existing room.
        The return_to_room method finds an existing room in the map dictionary by coordinates, records this room
        in the current rooms dictionary map of doors called doors, records the current room in the room about to be
        entered's dictionary map of doors, and changes the user's location to the room to which they are returning.
        """

        return_room = self.map[new_coordinates]
        self.player.location.memory[head] = return_room
        return_room.memory[record] = self.player.location
        self.player.location = return_room

    def create_room(self, new_coordinates, record, head):
        """
        The create_room method runs when a user goes to enter a new, unknown room.  The method instantiates a new,
        unique Room, records the new Room object by coordinates in the dictionary map, records the new Room in
        the current Room's dictionary of doors, records the current room in the new Room's dictionary of doors, and
        changes the player's current location to the new Room.
        """
        new = Room(new_coordinates)  # Instantiates a new Room with the unique coordinates.
        self.map[new_coordinates] = new
        self.player.location.memory[head] = new  # Records the new Room in the dictionary of the current Room.
        new.memory[record] = self.player.location  # Records the old room in the new room's doors dictionary.
        self.player.location = new  # Changes the player to the new room.

    def move(self):

        """
        The move method:
        1. gets user's choice of direction as head.
        2. first if statement checks to see if the current Room has a door in that direction.
        3. second if statement checks to see if the current Rooms map of doors knows what Room is in that direction
        4. if so, player's location Room changes to that Room
        5. else, the coordinates for the Room the player wants to enter is found as (x, y)using a simple math formula
        6. if the coordinates already exists in the Game map, the player's location changes to the existing Room
        7. else, a new Room is created and the user's location changes to the new Room
        """

        head = input("Which direction do you want to go? ")  # user chooses from available directions


        if head in self.player.location.memory.keys(): #Does Room have a door in that direction?
            if isinstance(self.player.location.memory[head], Room): #Has it been entered from this Room?
                self.player.location = self.player.location.memory[head] #If yes, return to that Room.
                #What if player has circled back around to an already visited, existing Room?  

            else:
                new_coordinates, record = self.map_room(head) #Finds coordinates and reverse direction for next Room.

                if new_coordinates in self.map.keys(): #Has the user been in this Room before?
                    self.return_to_room(new_coordinates, record, head) #Return to the preexisting Room and records.

                else:
                    self.create_room(new_coordinates, record, head) #Creates a new Room.


    def run_game(self):

        """
        Shows user a game menu and lets user enter inputs.
        """

        while True: #Keeps menu running.
            self.player.location.see_room()
            choice = input("""\n1. Move to another room. >>> """)
            if choice == "1": #Allows choice of a move.
                self.move()

this_game = Game()
this_game.run_game()
