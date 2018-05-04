from rgkit import rg

TARGET = (5, 5)


class Robot:
    def act(self, game):
        if self.location == TARGET:
            return ['guard']
        return ['move', rg.toward(self.location, TARGET)]
