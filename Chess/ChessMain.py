"""
This is our main driver file.  This is responsible for handling user input, displaying current GameState  object.
"""

import pygame as p
from Chess import ChessEngine

WIDTH = 512
HEIGHT = 512  # change to 400 if it doesn't look good
DIMENSION = 8  # chess board dimensions 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}  # global variable

'''
Initialize a global dictionary of images. This is called exactly once in main.
'''


def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bK', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note: we can access an image by saying 'IMAGES['wp']'
    # p.transform.scale will make images the right size


"""
This will be the main driver for the code.  This will handle user input and and updating the graphics
"""


def main():
    # initialize pygame
    p.init()
    # screen variable
    screen = p.display.set_mode((WIDTH, HEIGHT))
    # clock variable
    clock = p.time.Clock()
    # fill screen with color white, not necessary later on
    screen.fill(p.Color("white"))
    # create game state, gives access to variables in ChessEngine like board for example
    gs = ChessEngine.GameState()

    # example to print chess board
    # print(gs.board)

    # load in images. do this only once, before the while loop
    load_images()
    running = True
    while running:
        # clear event queue
        for e in p.event.get():
            # to quit game
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()

"""
Responsible for all the graphics within a current game state.
"""
def draw_game_state(screen,gs):
    # draws the squares on the board
    draw_board(screen)
    # draw pieces on top of those squares
    # can add in piece highlighting or move suggestions later
    draw_pieces(screen,gs.board)

"""
Draws the squares on the board. Top left square is always white, bottom right square as well.
"""
def draw_board(screen):
    # two colors picked for chess board, white and grey, not black because the pieces will be hard to see
    colors = [p.Color("white"), p.Color("grey")]
    # nested for loop, r = rows / c = columns
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            # gives us the remainder and tells us whether the square is even or odd
            # white squares are even (remainder 0) , dark squares are odd (remainder 1)
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))





"""
Draws the pieces on the board using the current game states board variable (GameState.board)
"""
def draw_pieces(screen, board):
    pass

if __name__ == "__main__":
    main()
