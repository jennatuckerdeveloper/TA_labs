
class Rooms:
    def __init__(self):
        # room_names = ['hall', 'hall', 'hall', 'lair', 'den']

        self.name = random.choice(room_names)
        room_names.remove(self.name)
        self.enemies = [enemies[random.randint(0, 1)]]
        self.items = items[random.randint(0, 1)]
        print(room_names)
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