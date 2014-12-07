class Game():
    def __init__(self, player):
        self.player = player
        self.answered = 0

    def calc_score(self):
        return self.answered ** 2
