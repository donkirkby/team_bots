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

        closest_target = None
        closest_distance = 1000000
        for target in game.robots.values():
            if target.player_id != self.player_id:
                distance = rg.dist(self.location, target.location)
                if distance < closest_distance:
                    closest_target = target
                    closest_distance = distance

        return ['move', rg.toward(self.location, closest_target.location)]
        # if self.location == self.target:
        #     return ['guard']
        # return ['move', rg.toward(self.location, self.target)]


