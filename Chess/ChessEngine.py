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

        self.move_functions = {'p': self.get_pawn_moves, 'R': self.get_rook_moves, 'N': self.get_knight_moves,
                               'B': self.get_bishop_moves, 'Q': self.get_queen_moves, 'K': self.get_king_moves}

        # field to determine who's turn it is
        self.white_to_move = True

        # field that keeps track of what moves have currently taken place
        self.move_log = []

    """
    Takes a Move as a parameter and executes it. (this does not work for castling, pawn promotion and en-passant)
    """

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"  # when we move a piece we leave behind an empty space
        self.board[move.end_row][move.end_col] = move.piece_moved  # moves piece to ending position
        self.move_log.append(move)  # can log the moves to be able to undo them later, or display the history of moves
        self.white_to_move = not self.white_to_move  # switch turns

    """
    Undo the last move made
    """

    def undo_move(self):
        if len(self.move_log) != 0:  # make sure that there is a move to undo or else it will throw an error
            move = self.move_log.pop()
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
        moves = []
        for r in range(len(self.board)):  # number of rows
            for c in range(len(self.board[r])):  # number of columns in given row
                turn = self.board[r][c][0]
                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
                    piece = self.board[r][c][1]
                    self.move_functions[piece](r, c, moves)  # calls the appropriate move function based on piece type
        return moves

    """
    Get all the pawn moves for the pawn located at row, column and add these moves to the list
    """

    def get_pawn_moves(self, r, c, moves):
        if self.white_to_move:  # white pawn moves
            if self.board[r - 1][c] == "--":  # one square pawn advance
                moves.append(Move((r, c), (r - 1, c), self.board))
                if r == 6 and self.board[r - 2][c] == "--":  # two square pawn advance
                    moves.append(Move((r, c), (r - 2, c), self.board))
            if c - 1 >= 0:  # captures to the left
                if self.board[r - 1][c - 1][0] == 'b':  # enemy piece to capture
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))
            if c + 1 <= 7:  # captures to the right
                if self.board[r - 1][c + 1][0] == 'b':  # enemy piece to capture
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))

        else:  # black pawn moves
            if self.board[r + 1][c] == "--":  # one square pawn advance
                moves.append(Move((r, c), (r + 1, c), self.board))
                if r == 1 and self.board[r + 2][c] == "--":  # two square pawn advance
                    moves.append(Move((r, c), (r + 2, c), self.board))
            if c - 1 >= 0:  # captures to the left
                if self.board[r + 1][c - 1][0] == 'w':  # enemy piece to capture
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))
            if c + 1 <= 7:  # captures to the right
                if self.board[r + 1][c + 1][0] == 'w':  # enemy piece to capture
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))
        # add pawn promotions later


    """
    Get all the rook moves for the rook located at row, column and add these moves to the list
    """

    def get_rook_moves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))  # up, left, down, right
        enemy_color = 'b' if self.white_to_move else 'w'
        for d in directions:
            for i in range(1, 8):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:  # on board
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--':  # empty space valid
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:  # enemy piece valid
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                        break
                    else:  # friendly piece invalid
                        break
                else:  # off board
                    break

    """
    Get all the knight moves for the knight located at row, column and add these moves to the list
    """

    def get_knight_moves(self, r, c, moves):
        knight_moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        ally_color = 'w' if self.white_to_move else 'b'
        for m in knight_moves:
            end_row = r + m[0]
            end_col = c + m[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != ally_color:  # not an ally piece (empty or enemy's)
                    moves.append(Move((r, c), (end_row, end_col), self.board))

    """
    Get all the bishop moves for the bishop located at row, column and add these moves to the list
    """

    def get_bishop_moves(self, r, c, moves):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))  # top left, bottom left, top right, bottom right
        enemy_color = 'b' if self.white_to_move else 'w'
        for d in directions:
            for i in range(1, 8):  # bishop can move a max of 7 squares
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:  # is it on the board
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--':  # empty space valid
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:  # enemy piece valid
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                        break
                    else:  # friendly piece invalid
                        break
                else:  # off board
                    break

    """
    Get all the queen moves for the queen located at row, column and add these moves to the list
    """

    def get_queen_moves(self, r, c, moves):
        pass

    """
    Get all the king moves for the king located at row, column and add these moves to the list
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
