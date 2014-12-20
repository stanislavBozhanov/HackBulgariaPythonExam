import unittest
from game import Game


class GameTests(unittest.TestCase):
    def setUp(self):
        self.ticky = Game('X', 'O')

    def test_init(self):
        self.assertEqual('X', self.ticky.py)
        self.assertEqual('O', self.ticky.cp)
        self.assertEqual([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], self.ticky.board)
        self.assertEqual(self.ticky.turns, 9)

    def test_field_taken(self):
        self.ticky.board[1][1] = '&'
        self.assertTrue(self.ticky.field_taken(1, 1))
        self.assertFalse(self.ticky.field_taken(2, 2))

    def test_field_exists(self):
        self.assertFalse(self.ticky.field_exists(3, 3))
        self.assertTrue(self.ticky.field_exists(1, 1))

    def test_player_puts_mark(self):
        self.ticky.player_puts_mark(1, 1)
        self.assertEqual(self.ticky.board[1][1], 'X')

    def test_computer_puts_mark(self):
        self.ticky.computer_puts_mark(1, 1)
        self.assertEqual(self.ticky.board[1][1], 'O')


if __name__ == '__main__':
    unittest.main()
