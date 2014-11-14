__author__ = 'macharir'

import unittest

import Game


class MyTestCase(unittest.TestCase):
    game = Game

    def test_move_left(self):
        b = [0]*16
        b[1] = 2
        b[2] = 2

        self.game.make_move(b,self.game.LEFT)
        self.assertTrue(b==[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    def test_move_right(self):
        b = [0]*16
        b[1] = 2
        b[2] = 2

        self.game.make_move(b,self.game.RIGHT)
        self.assertTrue(b==[0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0])

    def test_move_up(self):
        b = [0]*16
        b[1] = 2
        b[5] = 2
        self.game.make_move(b,self.game.UP)
        self.assertTrue(b==[0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    def test_move_down(self):
        b = [0]*16
        b[1] = 2
        b[5] = 2
        self.game.make_move(b,self.game.DOWN)
        self.assertTrue(b==[0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0])


if __name__ == '__main__':
    unittest.main()
