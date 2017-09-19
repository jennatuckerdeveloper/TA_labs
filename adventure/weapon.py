"""
*   Weapon
    * Location (or None if picked up)
    * Damage
"""

class Weapon:
    def __init__(self, name, location, damage):
        self.name = name
        self.location = location
        self.damage = damage

    def __str__(self):
        return self.name