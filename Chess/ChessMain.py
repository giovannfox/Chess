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
        IMAGES[piece] = p.image.load("images/" + piece + ".png")
