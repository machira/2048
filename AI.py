__author__ = 'Raymond Machira <raymond.machira@gmail.com>'

from Board import Board
from Game import Game

game = Game()
moves = game.MOVES



def evaluate_move(board, move, depth=4):
    if depth < 0:
        return board.score
    score = 0
    best_move = 0
    possible_new_cells = Board.possible_new_pieces()
    for piece, cell, probability in possible_new_cells:

    for move in Game.MOVES:

    evaluate_move(board, depth=depth-1)


def main():
    board = Board()
