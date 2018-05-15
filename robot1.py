from rgkit import rg


class Robot:
    def __init__(self):
        self.target = (10, 10)

    def act(self, game):
        if self.location == self.target:
            return ['guard']
        return ['move', rg.toward(self.location, self.target)]
