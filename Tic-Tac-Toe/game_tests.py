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

if __name__ == '__main__':
    unittest.main()
