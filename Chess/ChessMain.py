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

    # example
    print(gs.board)


main()
