class TicTacToe(object):
    """docstring for TicTacToe"""
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def print_board(self):
        for line in self.board:
            print(line)


def main():
    tic = TicTacToe()
    tic.print_board()

if __name__ == '__main__':
    main()
