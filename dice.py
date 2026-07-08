from random import randint

class Dice:
    """chooses a num randomly"""
    def __init__(self, die_sides=6):
        self.num_sides = die_sides

    def roll(self):
        """rolls a random num"""
        return randint(1, self.num_sides)