from random import randint


class Dice_model:
    def __init__(self, times: int = 1) -> None:
        self.times = times

    def roll_dice(self):
        current = 0
        for dice in range(self.times):
            current += randint(1, 6)
        return current
