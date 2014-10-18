__author__ = 'Raymond Machira <raymond.machira@gmail.com>'

###
### A 2048 solver, using MiniMax with A-B pruning.
###
import random, itertools
# left right up down
LEFT = -1
RIGHT = 1
UP = -1
DOWN = 1
MOVES = [LEFT, RIGHT, UP, DOWN]

class Board():
    # Makes an NxN board
    board_size = 4
    board = [None] * board_size
    for i in range(board_size):
        board[i] = [0] * board_size

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



# move across all unoccupied cells
# Check for any similar cells and collapse sequentially.
# Move across empty cells once more

def moveLEFTRIGHT(board, move):
    """
    :param board:
    :param move:
    :return:
    """

    # empty_cells = board.empty_cells()
    occupied_cells = board.occupied_cells()
    print occupied_cells
    # works only for left moves for now.
    for cell in occupied_cells:
        new_pos = (-1,-1)
        new_col = cell[1]+move
        while(-1 < new_col < board.board_size):
            if board.board[cell[0]][new_col] == 0:
                new_pos = (cell[0],new_col)
            else:
                break
            new_col = new_col + move
        # move
        if new_pos != (-1,-1):
            item = board.board[cell[0]][cell[1]]
            board.board[cell[0]][cell[1]] = 0
            board.board[new_pos[0]][new_pos[1]] = item

    return board


def moveUPDOWN(board, move):
    """
    :param board:
    :param move:
    :return:
    """

    # empty_cells = board.empty_cells()
    occupied_cells = board.occupied_cells()
    print occupied_cells
    # works only for left moves for now.
    for cell in occupied_cells:
        new_pos = (-1,-1)
        new_row = cell[0]+move
        while(-1 < new_row < board.board_size):
            if board.board[new_row][cell[1]] == 0:
                new_pos = (new_row,cell[0])
            else:
                break
            new_row = new_row + move
        # move
        if new_pos != (-1,-1):
            item = board.board[cell[0]][cell[1]]
            board.board[cell[0]][cell[1]] = 0
            board.board[new_pos[0]][new_pos[1]] = item

    return board

def test_move():
    board = Board()

    board.board[0][1] = 2
    board.board[0][3] = 2

    moveLEFTRIGHT(board,LEFT)
    assert(board.board == [[2,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

    moveLEFTRIGHT(board,RIGHT)
    assert(board.board == [[0,0,2,2],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

if __name__ == '__main__':
    # board = Board()
    #
    # random_cell = board.random_empty_cell()
    # random_cell2 = board.random_empty_cell()
    #
    # board.board[random_cell[0]][random_cell[1]] = 2
    # board.board[random_cell2[0]][random_cell2[1]] = 2
    #
    # for row in board.board:
    #     print row
    #
    # b = moveLEFTRIGHT(board,RIGHT).board
    test_move()

    # for row in b:
    #     print row