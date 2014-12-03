__author__ = 'Raymond Machira <raymond.machira@gmail.com>'
from time import sleep
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
WINNING_TILE = 2048
WEIGHTED_PIECES = [(2, 75), (4, 25)]#, (8, 12.5), (16, 6.25), (32, 6.25)]
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
                score_increment += (board[cell]+board[cell])
            else:
                break
        if move_to != cell:
            board[move_to] +=  board[cell]
            board[cell]  = 0 # make the old cell empty

    return board, number_smashes, score_increment, move


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

def show_board(board):
    i = 0
    while i < len(board):
        print board[i],' ',board[i+1],' ',board[i+2],' ',board[i+3],'\n'
        i += BOARD_SIZE
    print '\n'

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
    '''

    :param board:
    :return:
    '''
    best_move = MOVES[0]
    max_score = 0
    for move in MOVES:
        board2, number_smashes, score_increment,move  = make_move(board[:],move)
        if score_increment > max_score:
            best_move = move
            max_score = score_increment

    # MOVES = [LEFT, RIGHT, UP, DOWN]
    return make_move(board,best_move)


def monotonicity_strategy(board):
    best_move = random.choice(MOVES)
    best_monotonicity = float('Inf')
    for move in MOVES:
        board2 = make_move(board[:],move)[0]
        mon = most_monotonic_corner(board2)
        if mon < best_monotonicity:
            best_move = move
            best_monotonicity = mon

    return make_move(board, best_move)


def most_monotonic_corner(board):
    '''
    Evaluates the quality of a board based on the monotonicity of it's tiles towards a corner
    :param board:
    :return: the lowest scoring corner, in terms of monotonicity. A board with a lower score is more monotonous.
    '''
    left_limits = [BOARD_SIZE * i for i in range(0, BOARD_SIZE)]
    bottom_limits = [i for i in range(BOARD_SIZE * (BOARD_SIZE-1), BOARD_SIZE*BOARD_SIZE)]
    right_limits = [(BOARD_SIZE * i)-1 for i in range(1, BOARD_SIZE+1)]
    top_limits = range(0,BOARD_SIZE)

    best_corner = float('Inf')
    corners = [(left_limits, bottom_limits, -1, BOARD_SIZE),(right_limits, bottom_limits, 1, BOARD_SIZE),
               (right_limits, top_limits, 1, -1*BOARD_SIZE), (left_limits, top_limits, -1, -1*BOARD_SIZE)]
    for corner in corners:
        l1, l2, x, y = corner
        score = monotonicity(board, l1, l2, x, y, best_corner)
        # best possible score, no need to test more corners
        if score == 0: return score

        best_corner = min(score, best_corner)

    return best_corner

def monotonicity(board, limits1, limits2, xDelta, yDelta, minScore=float('Inf')):
    '''
    Calculates the monotonicity of a board, towards a given corner. A corner is detected by an index that
    appears in both limits. The xDelta is the direction of change of indices along the x axis. The yDelta is along
    the y-axis.
    Here is a perfectly monotonous board (towards the bottom right corner)
    3 2 1 0
    4 3 2 1
    5 4 3 2
    6 5 4 3

    A score is calculated based on how many cells are out of place with respect to each other. So, for instance,
    if the square (3,0) was not 6 as above, but was 4, the board would score 2 - one for each of the 5s surrounding
    (3,0)
    :param board: the board to score
    :param limits1: side bound
    :param limits2: upper or lower bound
    :param xDelta: what direction to compare, up or down
    :param yDelta: what direction to compare, left or right.
    :return: the number of cells that are out of place in relation to each other.
    '''
    score = 0
    for x,i in enumerate(board):
        # this run will be no better than an already run score, just return
        if score == minScore:
            break
        # skip the corner
        if x in limits1 and x in limits2:
            continue

        if x in limits1:
            if i > board[x+yDelta]: score += 1
        elif x in limits2:
            if i > board[x+xDelta]: score += 1
        else:
            if i > board[x+xDelta]: score+=1
            if i > board[x+yDelta]: score+=1

    return score


if __name__ == '__main__':
    num_iterations = 10000

    strategies = [(monotonicity_strategy,'most_monotonic_move.csv')]
        # , (make_random_move,'random_move.csv'),
        #           (make_max_scoring_move, 'max_scoring_move.csv')


    if len(sys.argv) > 1:
        num_iterations = int(sys.argv[2])

    for strategy,file_name in strategies:
        # prepare results file with appropriate headings
        with open(file_name, 'w') as results_file:
            results_file.write("Game_Won,Max_block,Num_moves,Score,Num_Smashes\n")

        for iter in range(0,num_iterations):
            board = new_board(board_size=4)
            num_moves_made = 0
            score = 0
            smashes = 0
            while not game_lost(board):
                #  board, number_smashes, score_increment
                # show_board(board)
                board2, number_smashes, score_increment, move = strategy(board[:])
                # useless move?
                while board2 == board:
                    board2, number_smashes, score_increment, move = make_move(board2,random.choice(MOVES))

                # print 'making move: ', 'LEFT' if move==MOVES[0] else 'RIGHT' if move==MOVES[1] else 'UP' if move == MOVES[2] else 'DOWN'
                board = board2
                # show_board(board)
                # sleep(5)

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
