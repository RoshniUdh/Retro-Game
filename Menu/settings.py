import pygame
import sys
import time
import random
from os import path
from settings import *

# General settings
TITLE = "Homerun"
FONT = "fonts\\prstart.ttf"
FPS = 60

DIR = path.dirname(__file__)
IMAGE_DIR = path.join(DIR, 'images')
SOUND_DIR = path.join(DIR, 'sound')

FILENAME_START_SCREEN = "start_screen.png"
FILENAME_INSTRUCTIONS_SCREEN = "instructiescherm_homerun.png"
FILENAME_GAME_OVER_SCREEN = "gameover_homerun.png"
FILENAME_HIGHSCORE = "highscore.txt"

FILENAME_MUSIC = "minigame_soundtrack.mp3"
FILENAME_BACKGROUND = "black_background.png"
FILENAME_SPRITESHEET = "spritesheet.png"
FILENAME_BALL = "Naamloos2.ico"

SCREEN_WIDTH_LVL0 = 480
SCREEN_HEIGHT_LVL0 = 600
SCREEN_WIDTH_LVL1 = 1280
SCREEN_HEIGHT_LVL1 = 720
SCREEN_WIDTH_LVL2 = 640
SCREEN_HEIGHT_LVL2 = 480
SCREEN_WIDTH_LVL3 = 480
SCREEN_HEIGHT_LVL3 = 600
SCREEN_WIDTH_LVL4 = 1024
SCREEN_HEIGHT_LVL4 = 695
SCREEN_WIDTH_LVL5 = 640
SCREEN_HEIGHT_LVL5 = 480
SCREEN_WIDTH_LVL6 = 600
SCREEN_HEIGHT_LVL6 = 500
SCREEN_SIZE   = 640,480

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
PURPLE    = (255,   0, 255)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)

# Object dimensions
BRICK_WIDTH   = 60
BRICK_HEIGHT  = 15
PADDLE_WIDTH  = 60
PADDLE_HEIGHT = 12
BALL_DIAMETER = 16
BALL_RADIUS   = BALL_DIAMETER / 2

MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
MAX_BALL_X   = SCREEN_SIZE[0] - BALL_DIAMETER
MAX_BALL_Y   = SCREEN_SIZE[1] - BALL_DIAMETER

# Paddle Y coordinate
PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 10

# State constants
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3