__author__ = 'Raymond Machira <raymond.machira@gmail.com>'

# ##
### A 2048 solver, using MiniMax with A-B pruning.
###
import random, sys
# move across all unoccupied cells
# Check for any similar cells and collapse sequentially.
# Move across empty cells once more


# left right up down
LEFT = -1
RIGHT = 1
UP = -4
DOWN = 4
MOVES = [LEFT, RIGHT, UP, DOWN]
BOARD_SIZE = 4
WINNING_TILE = 1024
WEIGHTED_PIECES = [(2, 50), (4, 25), (8, 12.5), (16, 6.25), (32, 6.25)]
# WEIGHTED_PIECES = [(2, 100)]#, (4, 25), (8, 12.5), (16, 6.25), (32, 6.25)]

def make_move(board, move):
    """
    :param board: the game board on which to make a move
    :param move: the move to be made
    :return: the board, with the move made, and the score populated as the last item.
    """
    limits = []
    # number of smashes for this move
    number_smashes = 0
    score_increment = 0

    if move == LEFT:
        limits = [BOARD_SIZE * i for i in range(0, BOARD_SIZE)]
    elif move == RIGHT:
        limits = [(BOARD_SIZE * i)-1 for i in range(1, BOARD_SIZE+1)]
    elif move == UP:
        limits =  range(0, BOARD_SIZE)
    elif move == DOWN:
        limits = [i for i in range(BOARD_SIZE * (BOARD_SIZE-1), BOARD_SIZE*BOARD_SIZE)]


    # empty_cells = board.empty_cells()
    occupied = occupied_cells(board)
    # sort the cells to start at the right end
    occupied.sort(reverse= move > 0)
    for cell in occupied:
        move_to = cell
        while move_to not in limits:
            if board[move_to+move] == 0:
                move_to += move
            # neighbouring cell is actually the same as this one, a smash can take place/we can move one more.
            elif board[move_to+move] == board[cell]:
                number_smashes += 1
                move_to += move
                # also increment our score. I use addition instead of multiplication- a small optimization.
                score_increment += board[cell]+board[cell]
            else:
                break
        if move_to != cell:
            board[move_to] +=  board[cell]
            board[cell]  = 0 # make the old cell empty

    return board, number_smashes, score_increment


def random_empty_cell(board):
    empty_cell = empty_cells(board)
    if len(empty_cell):
        return random.choice(empty_cells)


def empty_cells(board):
    return [i for i in range(0, len(board)) if board[i] == 0]

def occupied_cells(board):
    return [i for i in range(0,len(board)) if board[i] != 0]

def game_lost(board):
    return len(empty_cells(board)) == 0


def game_won(board):
    return max(board) >= WINNING_TILE


## simply returns a possible block
def random_block():
    total = sum(w for c, w in WEIGHTED_PIECES)
    r = random.uniform(0, total)
    upto = 0
    for c, w in WEIGHTED_PIECES:
        if upto + w > r:
            return c
        upto += w

def new_board(board_size=BOARD_SIZE):
    board = [0]*(board_size*board_size)
    return random_block_spawn(board)

def random_block_spawn(board):
    cell = random.choice(empty_cells(board))
    board[cell] = random_block()
    return board

def make_random_move(board):
    move = random.choice(MOVES)
    return make_move(board,move)

def make_max_scoring_move(board):
    best_move = MOVES[0]
    max_score = 0
    for move in MOVES:
        board, number_smashes, score_increment  = make_move(board[:],move)
        if score_increment > max_score:
            best_move = move

    return make_move(board,best_move)

# def evaluate_move(board, move, depth=4):
#     if board.game_won: return float("Infinity")
#     # this game ends in loss
#     elif board.game_over: return float("-Infinity")
#     # stops recursion
#     elif depth < 0:
#         return board.score
#
#     possible_new_cells = possible_new_pieces()
#     for piece, cell, probability in possible_new_cells:
#
#     for move in MOVES:
#
#         evaluate_move(board, depth=depth-1)


if __name__ == '__main__':
    num_iterations = 10000

    strategies = [(make_max_scoring_move,'max_scoring_move.csv'), (make_random_move,'random_move.csv'),
                  (make_max_scoring_move, 'max_scoring_move.csv')

                ]

    if len(sys.argv) > 1:
        num_iterations = int(sys.argv[2])

    for strategy,file_name in strategies:
        # prepare results file with appropriate headings
        with open(file_name, 'w') as results_file:
            results_file.write("Game_Won,Max_block,Num_moves,Score\n")

        for iter in range(0,num_iterations):
            board = new_board(board_size=4)
            num_moves_made = 0
            score = 0
            smashes = 0
            while not game_lost(board):
                board, number_smashes, score_increment = strategy(board)
                score += score_increment
                smashes += number_smashes
                num_moves_made += 1
                board = random_block_spawn(board)
                # if game_won(board):
                #     break

            win = game_won(board)
            max_block = max(board)

            with open(file_name, 'a') as results_file:
                results_file.write("{0},{1},{2},{3},{4}\n".format(win, max_block, num_moves_made, score, smashes))
