__author__ = 'macharir'

import unittest
from Board import Board
from Game import  Game

class MyTestCase(unittest.TestCase):
    game  = Game()

    def test_move_left(self):
        board1 = Board()
        board1.board[0][1]=2
        board1.board[0][3]=2

        self.game.moveLEFTRIGHT(board1,self.game.LEFT)
        self.assertTrue(board1.board==[[4,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

    def test_move_right(self):
        board2 = Board()
        board2.board[0][1]=2
        board2.board[0][3]=2
        self.game.moveLEFTRIGHT(board2,self.game.RIGHT)
        self.assertTrue(board2.board==[[0,0,0,4],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

    def test_move_up(self):
        board3 = Board()
        board3.board[0][2]=2
        board3.board[1][2]=2
        self.game.moveUPDOWN(board3,self.game.UP)
        self.assertTrue(board3.board==[[0,0,4,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

    def test_move_down(self):
        board4 = Board()
        board4.board[0][2]=2
        board4.board[1][2]=2
        self.game.moveUPDOWN(board4,self.game.DOWN)
        self.assertTrue(board4.board==[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,4,0]])


if __name__ == '__main__':
    unittest.main()
