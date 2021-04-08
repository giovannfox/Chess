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

    """
    Takes a Move as a parameter and executes it. (this does not work for castling, pawn promotion and en-passant)
    """

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"  # when we move a piece we leave behind an empty space
        self.board[move.end_row][move.end_col] = move.piece_moved  # moves piece to ending position
        self.moveLog.append(move)  # can log the moves to be able to undo them later, or display the history of moves
        self.white_to_move = not self.white_to_move  # switch turns

    """
    Undo the last move made
    """

    def undo_move(self):
        if len(self.moveLog) != 0:  # make sure that there is a move to undo or else it will throw an error
            move = self.moveLog.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move  # switch turns back

    """
    All moved considering checks
    """

    def get_valid_moves(self):
        return self.get_all_possible_moves()  # will modify later to account for checking

    """
    All moves without considering checks
    """

    def get_all_possible_moves(self):
        moves = [Move((6, 4), (4, 4), self.board)]
        for r in range(len(self.board)):  # number of rows
            for c in range(len(self.board[r])):  # number of columns in given row
                turn = self.board[r][c][0]
                if (turn == 'w' and self.white_to_move) and (turn == 'b' and not self.white_to_move):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.get_pawn_moves(r, c, moves)
                    elif piece == 'R':
                        self.get_rook_moves(r, c, moves)
                    elif piece == 'N':
                        self.get_rook_moves(r, c, moves)
                    elif piece == 'B':
                        self.get_rook_moves(r, c, moves)
                    elif piece == 'Q':
                        self.get_rook_moves(r, c, moves)
                    elif piece == 'K':
                        self.get_rook_moves(r, c, moves)
        return moves

    """
    Get all the pawn moves for the pawn located at row, column and add these moves to the list
    """

    def get_pawn_moves(self, r, c, moves):
        pass

    """
    Get all the rook moves for the pawn located at row, column and add these moves to the list
    """

    def get_rook_moves(self, r, c, moves):
        pass

    """
    Get all the knight moves for the pawn located at row, column and add these moves to the list
    """

    def get_knight_moves(self, r, c, moves):
        pass

    """
    Get all the bishop moves for the pawn located at row, column and add these moves to the list
    """

    def get_bishop_moves(self, r, c, moves):
        pass

    """
    Get all the queen moves for the pawn located at row, column and add these moves to the list
    """

    def get_queen_moves(self, r, c, moves):
        pass

    """
    Get all the king moves for the pawn located at row, column and add these moves to the list
    """

    def get_king_moves(self, r, c, moves):
        pass


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
        self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        print(self.move_id)

    """"
    Overriding the equals method
    """

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False

    def get_chess_notation(self):
        # I can add to make it real chess notation later, atm this is rank/file notation
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]
