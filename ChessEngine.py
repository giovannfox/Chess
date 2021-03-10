"""
This class is responsible for storing all the information about the current state of a chess game.
It will also be responsible for determining the valid moves at the current state.  It will also keep a move log.
"""


class GameState:
    # constructor
    def __init__(self):
        # 2 dimensional list from white's perspective, 8x8 2d list, each element of the list has 2 characters
        # first character represents the color of the piece. b = black, w = white
        # second character represents the type. R = rook, N = knight, B = bishop, Q = queen, K = king
        # empty spaces are a 2 dash string in order to parse the string in the same way we would parse another string
        # If we used a 0 instead, for the empty spaces, we would have to convert from ints to string, more work.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        # field to determine who's turn it is
        self.whiteToMove = True

        # field that keeps track of what moves have currently taken place
        self.moveLog = []
