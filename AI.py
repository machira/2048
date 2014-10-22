__author__ = 'Raymond Machira <raymond.machira@gmail.com>'

from Board import Board
from Game import Game

game = Game()
moves = game.MOVES



def evaluate_move(board, move, depth=4):
    if depth < 0:
        return board.score
    score = 0
    evaluate_move(board, depth=depth-1)


def main():
    board = Board()
