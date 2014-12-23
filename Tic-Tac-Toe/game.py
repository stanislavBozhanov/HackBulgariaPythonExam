game_size = 3


class Game(object):
    """docstring for Game"""
    def __init__(self, players_mark, computers_mark):
        self.py = players_mark
        self.cp = computers_mark
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def all_fields_taken(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    return False
        return True

    def field_taken(self, row, col):
        return self.board[row][col] != ' '

    def field_exists(self, row, col):
        return 0 <= row and row <= 2 and 0 <= col and col <= 2

    def player_puts_mark(self, row, col):
        self.board[row][col] = self.py

    def computer_puts_mark(self, row, col):
        self.board[row][col] = self.cp

    def someone_wins(self, mark):
        for row in range(3):
            right_diag_win = True
            left_diag_win = True
            row_win = True
            col_win = True
            for col in range(3):
                if col + row == 3 and self.board[row][col] != mark:
                    right_diag_win = False
                if col == row and self.board[row][col] != mark:
                    left_diag_win = False
                if self.board[row][col] != mark:
                    row_win = False
                if self.board[col][row] != mark:
                    col_win = False
            return right_diag_win or left_diag_win or row_win or col_win

    def player_wins(self):