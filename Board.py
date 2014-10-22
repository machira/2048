__author__ = 'Raymond Machira <raymond.machira@gmail.com>'
import random, itertools


class Board():
    # Makes an NxN board
    board_size = 4

    def __init__(self):
        board = [None] * self.board_size
        for i in range(self.board_size):
            board[i] = [0] * self.board_size
        self.board = board

    def random_empty_cell(self):
        empty_cells = self.empty_cells()
        if len(empty_cells):
            return empty_cells[random.randrange(0,len(empty_cells))]

    def empty_cells(self):
        empty = []
        for i in range(0, self.board_size):
            for j in range(0,self.board_size):
                if self.board[i][j] == 0:
                    empty.append((i,j))
        return empty

    def occupied_cells(self):
        return [tpl for tpl in self.tuple_board() if tpl not in self.empty_cells()]

    def tuple_board(self):
        """
        returns a list of the board, as tuples
        """
        return list(itertools.chain(*[[(i,j) for i in range(0, self.board_size)] for j in range(0, self.board_size)]))


