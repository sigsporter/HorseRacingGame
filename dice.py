from random import randint

class Dice:
    """A class representing two six-sided dice."""

    def __init__(self):
        """Assume a six-sided die."""
        self.num_sides = 6

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides) + randint(1, self.num_sides)