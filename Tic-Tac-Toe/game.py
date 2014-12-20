class Game(object):
    """docstring for Game"""
    def __init__(self, players_mark, computers_mark):
        self.py = players_mark
        self.cp = computers_mark
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.turns = 9

    def field_taken(self, row, col):
        return self.board[row][col] != ' '

    def field_exists(self, row, col):
        return 0 <= row and row <= 2 and 0 <= col and col <= 2

    def player_puts_mark(self, row, col):
        self.board[row][col] = self.py

    def computer_puts_mark(self, row, col):
        self.board[row][col] = self.cp
