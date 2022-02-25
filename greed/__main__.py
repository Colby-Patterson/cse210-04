import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.character import Character
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)

def main():
    """satisfy python"""
    #create cast
    cast = Cast()

    #create player character
    x = int(MAX_X / 2)
    y = 0
    start_position = Point(x, y)

    character = Character()
    character.set_text('#')
    character.set_size(FONT_SIZE)
    character.set_axis(1)
    character.set_position(start_position)
    character.set_color(WHITE)

    cast.add_actor('character', character)

    #create banner
    banner = Actor()
    banner.set_text('Score: 0')
    banner.set_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))

    #start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()