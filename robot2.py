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

    # POSSIBLE_MOVES = [
    #     ("move",),
    #     ("move",),
    #     ("move",),
    #     ("move",),
    #     ("move",),
    #     ("guard",),
    #     ("attack", (1, 0)),
    #     ("attack", (-1, 0)),
    #     ("attack", (0, -1)),
    #     ("attack", (0, 1)),
    # ]

    POSSIBLE_MOVES = [
        "move",
        "move",
        "move",
        "move",
        "guard",
    ]

    def act(self, game):
        for bot_location, robot_info in game.robots.items():
            if robot_info.player_id == self.player_id:
                continue
            # Having reached here, we know this is an opposition robot.
            dx = bot_location[0] - self.location[0]
            dy = bot_location[1] - self.location[1]

            if abs(dx) + abs(dy) == 1:
                # The opponent bot is adjacent to us -- attack!
                return ["attack", (self.location[0] + dx, self.location[1] + dy)]

        # Having reached *here*, we know that there's nothing right to us, so pick a move at random.
        move = random.sample(self.POSSIBLE_MOVES, 1)[0]
        if move == "move":
            direction = rg.toward(self.location, self.RALLY_POINT)
            return ["move", direction]
        else:
            return ["guard"]

    # def act(self, game):
    #     move = self.choose_move(game)
    #
    #     def add(xy, dxdy):
    #         dx, dy = dxdy
    #         x, y = xy
    #         return (x + dx, y + dy)
    #
    #     if move[0] == "move":
    #         direction = rg.toward(self.location, self.RALLY_POINT)
    #         return ["move", direction]
    #     if move[0] == "attack":
    #         # import pdb; pdb.set_trace()
    #         pos = add(self.location, move[1])
    #         return ["attack", pos]
    #     return move

