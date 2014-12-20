class Game(object):
    """docstring for Game"""
    def __init__(self, players_mark, computers_mark):
        self.py = players_mark
        self.cp = computers_mark
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.turns = 9
