__author__ = 'Raymond Machira <raymond.machira@gmail.com>'

###
### A 2048 solver, using MiniMax with A-B pruning.
###
import random, itertools
from operator import itemgetter
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



def moveLEFTRIGHT(board, move, collapse=True):
    """
    :param board:
    :param move:
    :return:
    """

    # empty_cells = board.empty_cells()
    occupied_cells = board.occupied_cells()
    occupied_cells.sort(key=itemgetter(1), reverse= move==RIGHT)

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

    # collapses adjacent, similar values into the same cell, in the direction of the move.
    if(collapse):
        # for each occupied cell, except the first column, for left moves and last column for right moves
        # check the cell to its right or left, as necessary
        # update list of occupied cells
        cells = board.occupied_cells()
        for cell in [(row,col) for row,col in cells if (col != 0 and move==LEFT) or (col != board.board_size-1 and move ==RIGHT)]:
            # if they are similar
            if board.board[cell[0]][cell[1]] == board.board[cell[0]][cell[1]+move]:
                # double the value of the cell
                board.board[cell[0]][cell[1]+move] += board.board[cell[0]][cell[1]+move]
                board.board[cell[0]][cell[1]] = 0
        # clean up the board, with one last pass for
        moveLEFTRIGHT(board,move,collapse=False)

    return board

def moveUPDOWN(board, move, collapse = True):
    """
    :param board:
    :param move:
    :return:
    """

    # empty_cells = board.empty_cells()
    occupied_cells = board.occupied_cells()

    ## sort the occupied cells, depending on the direction of movement.

    occupied_cells.sort(key = itemgetter(0), reverse = move==DOWN)
    print occupied_cells
    # works only for left moves for now.
    for cell in occupied_cells:
        new_pos = (-1,-1)
        new_row = cell[0]+move
        while(-1 < new_row < board.board_size):
            if board.board[new_row][cell[1]] == 0:
                new_pos = (new_row,cell[1])
            else:
                break
            new_row = new_row + move
        # move
        if new_pos != (-1,-1):
            item = board.board[cell[0]][cell[1]]
            board.board[cell[0]][cell[1]] = 0
            board.board[new_pos[0]][new_pos[1]] = item

    if collapse:
        cells = board.occupied_cells()
        for cell in [(row,col) for row,col in cells if (row != 0 and move == UP) or (row != board.board_size-1 and move ==DOWN)]:
            # if they are similar
            if board.board[cell[0]][cell[1]] == board.board[cell[0]+move][cell[1]]:
                # double the value of the cell
                board.board[cell[0]+move][cell[1]] += board.board[cell[0]+move][cell[1]]
                board.board[cell[0]][cell[1]] = 0
        # clean up the board, with one last pass for
        moveUPDOWN(board,move,collapse=False)


    return board

def test_move_left():
    board1 = Board()
    board1.board[0][1] = 2
    board1.board[0][3] = 2

    moveLEFTRIGHT(board1,LEFT)
    assert(board1.board == [[4,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

def test_move_right():
    board2 = Board()
    board2.board[0][1] = 2
    board2.board[0][3] = 2
    moveLEFTRIGHT(board2,RIGHT)
    assert(board2.board == [[0,0,0,4],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

def test_move_up():
    board3 = Board()
    board3.board[0][2] = 2
    board3.board[1][2] = 2
    moveUPDOWN(board3,UP)
    assert(board3.board == [[0,0,4,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

def test_move_down():
    board4 = Board()
    board4.board[0][2] = 2
    board4.board[1][2] = 2
    moveUPDOWN(board4,DOWN)
    assert(board4.board == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,4,0]])
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
    test_move_left()
    test_move_right()
    test_move_down()
    test_move_up()

    # for row in b:
    #     print row