import unittest
from game import Game


class GameTests(unittest.TestCase):
    def setUp(self):
        self.ticky = Game('X', 'O')

    def test_init(self):
        self.assertEqual('X', self.ticky.py)
        self.assertEqual('O', self.ticky.cp)
        self.assertEqual([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], self.ticky.board)

    def test_field_taken(self):
        self.ticky.board[1][1] = '&'
        self.assertTrue(self.ticky.field_taken(1, 1))
        self.assertFalse(self.ticky.field_taken(2, 2))

    def test_field_exists(self):
        self.assertFalse(self.ticky.field_exists(3, 3))
        self.assertTrue(self.ticky.field_exists(1, 1))

    def test_all_fields_taken(self):
        self.ticky.board = [['O', 'X', 'O'], ['X', 'X', 'X'], ['O', 'O', 'X']]
        self.assertTrue(self.ticky.all_fields_taken())
        self.ticky.board = [['X', 'X', 'O'], ['X', ' ', 'X'], ['X', 'O', 'O']]
        self.assertFalse(self.ticky.all_fields_taken())

    def test_player_puts_mark(self):
        self.ticky.player_puts_mark(1, 1)
        self.assertEqual(self.ticky.board[1][1], 'X')

    def test_computer_puts_mark(self):
        self.ticky.computer_puts_mark(1, 1)
        self.assertEqual(self.ticky.board[1][1], 'O')

    def test_someone_wins(self):
        #row_win
        self.ticky.board = [['O', 'X', 'O'], ['X', 'X', 'X'], ['O', 'O', 'X']]
        self.
        #col_win
        self.ticky.board = [['O', 'X', 'O'], ['X', 'X', 'O'], ['O', 'X', 'X']]
        #left_diag_win
        self.ticky.board = [['X', 'O', 'O'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        #right_diag_win
        self.ticky.board = [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]

    def test_player_wins(self):
        self.ticky.board = [['O', 'X', 'O'], ['X', 'X', 'X'], ['O', 'O', 'X']]
        self.assertTrue(self.ticky.player_wins())
        self.ticky.board = [['O', 'X', 'O'], ['X', 'O', 'O'], ['X', 'O', 'X']]
        self.assertFalse(self.ticky.player_wins())

if __name__ == '__main__':
    unittest.main()
