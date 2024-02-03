class Horse:
    """A class to manage racing horses"""

    def __init__(self, lane, rolls_to_win):
        self.lane = lane
        self.position = 0
        self.rolls_to_win = rolls_to_win