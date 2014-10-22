__author__ = 'macharir'

import unittest

from Board import Board
from Game import Game


class MyTestCase(unittest.TestCase):
    game = Game()

    def test_move_left(self):
        board1 = Board(board_size=4)
        b = [0]*16
        b[1] = 2
        b[2] = 2
        board1.set_board(b)

        self.game.make_move(board1,self.game.LEFT)
        self.assertTrue(board1.board==[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    def test_move_right(self):
        board2 = Board()
        b = [0]*16
        b[1] = 2
        b[2] = 2
        board2.set_board(b)

        self.game.make_move(board2,self.game.RIGHT)
        self.assertTrue(board2.board==[0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0])

    def test_move_up(self):
        board3 = Board()
        b = [0]*16
        b[1] = 2
        b[5] = 2
        board3.set_board(b)
        self.game.make_move(board3,self.game.UP)
        self.assertTrue(board3.board==[0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    def test_move_down(self):
        board4 = Board()
        b = [0]*16
        b[1] = 2
        b[5] = 2
        board4.set_board(b)
        self.game.make_move(board4,self.game.DOWN)
        self.assertTrue(board4.board==[0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0])


if __name__ == '__main__':
    unittest.main()
