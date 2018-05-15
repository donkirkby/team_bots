import random

from rgkit import rg


class Robot:
    def __init__(self):
        self.target = (13, 13)


    possible_moves = [
        ["move", (0, 1)],
        ["move", (0, -1)],
        ["move", (1, 0)],
        ["move", (-1, 0)],
        ["guard"],
        ["attack", (1, 0)],
        ["attack", (-1, 0)],
        ["attack", (0, -1)],
        ["attack", (-1, 1)],
    ]

    def act(self, game):
        move = random.sample(self.possible_moves, 1)[0]

        def add(xy, dxdy):
            dx, dy = dxdy
            x, y = xy
            return (x + dx, y + dy)

        if move[0] =="move":
            new = add(self.location, move[1])
            direction = rg.toward(self.location, new)
            move[1] = direction
        if move[0] == "attack":
            pos = add(self.location, move[1])
            move[1] = pos
        return move

