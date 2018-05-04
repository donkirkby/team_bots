from rgkit import rg

TARGET = (13, 13)


class Robot:
    def act(self, game):
        if self.location == TARGET:
            return ['guard']
        return ['move', rg.toward(self.location, TARGET)]
