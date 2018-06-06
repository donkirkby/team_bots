from rgkit import rg


class Robot:
    def __init__(self):
        self.target = (7, 7)

    def act(self, game):
        enemies = []
        myx, myy = self.location
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                x = myx + dx
                y = myy + dy
                target = game.robots.get((x, y), None)
                if (target and
                        target.player_id != self.player_id and
                        (dx == 0 or dy == 0)):
                    enemies.append(target)

        weak_count = 0
        for enemy in enemies:
            if enemy.hp <= 15:
                weak_count = weak_count + 1
        if weak_count >= 2:
            return ['suicide']

        if enemies:
            return ['attack', enemies[0].location]

        if self.location == self.target:
            return ['guard']
        return ['move', rg.toward(self.location, self.target)]


