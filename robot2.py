import random

from rgkit import rg


class Robot(object):

    RALLY_RANGE = (5, 14)

    def __init__(self):
        while True:
            x = random.randint(*self.RALLY_RANGE)
            y = random.randint(*self.RALLY_RANGE)
            locations = rg.loc_types((x, y))
            target = set(['normal'])
            if locations != target:
                continue
            else:
                self.RALLY_POINT = x, y
                break

    POSSIBLE_MOVES = [
        ("move",),
        ("move",),
        ("move",),
        ("move",),
        ("move",),
        ("guard",),
        ("attack", (1, 0)),
        ("attack", (-1, 0)),
        ("attack", (0, -1)),
        ("attack", (0, 1)),
    ]

    def choose_move(self):
        move = random.sample(self.POSSIBLE_MOVES, 1)[0]
        return move


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
        move = self.choose_move()

        def add(xy, dxdy):
            dx, dy = dxdy
            x, y = xy
            return (x + dx, y + dy)

        if move[0] == "move":
            direction = rg.toward(self.location, self.RALLY_POINT)
            return ["move", direction]
        if move[0] == "attack":
            # import pdb; pdb.set_trace()
            pos = add(self.location, move[1])
            return ["attack", pos]
        return move

