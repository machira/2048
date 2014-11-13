__author__ = 'Raymond Machira <raymond.machira@gmail.com>'
import random
import itertools

###A board is encoded as an list of size N*N.

class Board():
    board_size = 4 # default
    score = 0

    def __init__(self, board_size=board_size):
        board = [0] * board_size
        self.board = board

    def set_board(self,board):
        self.board = board
        self.score = 0

    def random_empty_cell(self):
        empty_cells = self.empty_cells()
        if len(empty_cells):
            return random.choice(empty_cells)

    def empty_cells(self):
        return [i for i in self.board if self.board[i] == 0]

    def occupied_cells(self):
        return [i for i in range(0,len(self.board)) if self.board[i] != 0]