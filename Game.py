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
    UP = -1
    DOWN = 1
    MOVES = [LEFT, RIGHT, UP, DOWN]

    def moveLEFTRIGHT(self,board, move, collapse=True):
        """
        :param board:
        :param move:
        :return:
        """

        # empty_cells = board.empty_cells()
        occupied_cells = board.occupied_cells()
        occupied_cells.sort(key=itemgetter(1), reverse= move==self.RIGHT)

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
            for cell in [(row,col) for row,col in cells if (col != 0 and move==self.LEFT) or (col != board.board_size-1 and move ==self.RIGHT)]:
                # if they are similar
                if board.board[cell[0]][cell[1]] == board.board[cell[0]][cell[1]+move]:
                    # double the value of the cell
                    board.board[cell[0]][cell[1]+move] += board.board[cell[0]][cell[1]+move]
                    board.board[cell[0]][cell[1]] = 0
            # clean up the board, with one last pass
            self.moveLEFTRIGHT(board,move,collapse=False)

        return board

    def moveUPDOWN(self,board, move, collapse = True):
        """
        :param board:
        :param move:
        :return:
        """

        # empty_cells = board.empty_cells()
        occupied_cells=board.occupied_cells()

        ## sort the occupied cells, depending on the direction of movement.

        occupied_cells.sort(key=itemgetter(0), reverse=move==self.DOWN)
        print occupied_cells
        # works only for left moves for now.
        for cell in occupied_cells:
            new_pos = (-1,-1)
            new_row = cell[0]+move
            while(-1 < new_row < board.board_size):
                if board.board[new_row][cell[1]]==0:
                    new_pos=(new_row,cell[1])
                else:
                    break
                new_row=new_row + move
            # move
            if new_pos != (-1,-1):
                item = board.board[cell[0]][cell[1]]
                board.board[cell[0]][cell[1]] = 0
                board.board[new_pos[0]][new_pos[1]] = item

        if collapse:
            cells = board.occupied_cells()
            for cell in [(row,col) for row,col in cells if (row != 0 and move == self.UP) or (row != board.board_size-1 and move == self.DOWN)]:
                # if they are similar
                if board.board[cell[0]][cell[1]]==board.board[cell[0]+move][cell[1]]:
                    # double the value of the cell
                    board.board[cell[0]+move][cell[1]]+=board.board[cell[0]+move][cell[1]]
                    board.board[cell[0]][cell[1]]=0
            # clean up the board, with one last pass
            self.moveUPDOWN(board,move,collapse=False)


        return board