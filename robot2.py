import random

from rgkit import rg


class Robot:
    def __init__(self):
        self.target = (13, 13)

    possible_moves = [
        ["move", (-1, 1)],
        ["move", (-1, -1)],
        ["move", (1, 1)],
        ["move", (1, -1)],
        ["guard"],
        ["attack", (-1, 1)],
        ["attack", (-1, -1)],
        ["attack", (1, 1)],
        ["attack", (1, -1)],
        ["suicide"],
    ]

    def act(self, game):
        return random.sample(self.possible_moves, 1)
