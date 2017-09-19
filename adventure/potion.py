"""
*   Potion
    * Location
    * Health Restored

"""

class Potion:
    def __init__(self, name, location, potency):
        self.name = name
        self.location = location
        self.potency = potency

    def __str__(self):
        return "{} potion".format(self.name)