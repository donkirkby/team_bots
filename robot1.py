from rgkit import rg


class Robot:
    def __init__(self):
        self.target = (7, 7)

    def act(self, game):
    	myx, myy = self.location
    	for dx in (-1, 0, 1):
    		for dy in (-1, 0, 1):
    			x = myx + dx
    			y = myy + dy
    			target = game.robots.get((x, y), None)
    			if target and target.player_id != self.player_id:
    				return ['attack', (x, y)]
    	if self.location == self.target:
            return ['guard']
        return ['move', rg.toward(self.location, self.target)]
