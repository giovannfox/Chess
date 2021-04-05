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
        self.white_to_move = True

        # field that keeps track of what moves have currently taken place
        self.moveLog = []

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"  # when we move a piece we leave behind an empty space
        self.board[move.end_row][move.end_col] = move.piece_moved  # moves piece to ending position
        self.moveLog.append(move)  # can log the moves to be able to undo them later, or display the history of moves
        self.white_to_move = not self.white_to_move  # switch turns, now blacks turn


class Move:
    # dictionary that maps keys to value
    # key : value
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    # for loop that reverses the dictionary of items
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    def get_chess_notation(self):
        # I can add to make it real chess notation later, atm this is rank/file notation
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]
