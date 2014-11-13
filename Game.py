__author__ = 'Raymond Machira <raymond.machira@gmail.com>'

###
### A 2048 solver, using MiniMax with A-B pruning.
###
from operator import itemgetter
from Board import Board


# move across all unoccupied cells
# Check for any similar cells and collapse sequentially.
# Move across empty cells once more


class Game():
    # left right up down
    LEFT = -1
    RIGHT = 1
    UP = -4
    DOWN = 4
    MOVES = [LEFT, RIGHT, UP, DOWN]

    def make_move(self,board, move, collapse=True):
        """
        :param board:
        :param move:
        :return:
        """
        limits = []

        if move == self.LEFT:
            limits = [board.board_size * i for i in range(0,board.board_size)]
        elif move == self.RIGHT:
            limits = [(board.board_size * i)-1 for i in range(1,board.board_size+1)]
        elif move == self.UP:
            limits =  range(0,board.board_size)
        elif move == self.DOWN:
            limits = [i for i in range(board.board_size * (board.board_size-1), board.board_size*board.board_size)]


        # empty_cells = board.empty_cells()
        occupied_cells = board.occupied_cells()
        # sort the cells to start at the right end
        occupied_cells.sort(reverse= move > 0)
        for cell in occupied_cells:
            move_to = cell
            while(move_to not in limits):
                if board.board[cell+move] == 0 or board.board[cell+move] == board.board[cell]:
                    move_to += move
                else:
                    break
            if move_to != cell:
                board.board[move_to] +=  board.board[cell]
                board.board[cell]  = 0 # make the old cell empty

        return board