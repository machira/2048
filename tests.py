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


    def test_monotonicity(self):
        perf_board = board =[3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2, 6, 5, 4, 3]
        left_edge_indices = [0,4,8,12]
        right_edge_indices = [3,7,11,15]
        top_edge_indices = [0,1,2,3]
        bottom_edge_indices = [12,13,14,15]

        self.assertEqual(0, self.game.most_monotonic_corner(perf_board))

        # assert that that the best corner is the bottom left
        self.assertEqual(0, self.game.monotonicity(perf_board, left_edge_indices, bottom_edge_indices, -1, 4))
        self.assertEqual(24, self.game.monotonicity(perf_board, right_edge_indices, top_edge_indices, 1, -4)) # top right
        self.assertEqual(12, self.game.monotonicity(perf_board, left_edge_indices, top_edge_indices, -1, -4)) # top left
        self.assertEqual(12, self.game.monotonicity(perf_board, right_edge_indices, bottom_edge_indices, 1, 4)) # bottom right

if __name__ == '__main__':
    unittest.main()
