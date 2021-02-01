# @Author:srattigan
# @Date:2021-01-25 09:55:57
# @LastModifiedBy:srattigan
# @Last Modified time:2021-01-25 10:00:49

# -- IMPORTS --
import random
import math
import arcade
from settings import *
from box import Box

# -- GLOBALS/CONSTANTS


# -- CLASSES/FUNCTIONS

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        :param width:
        :param height:
        """
        super().__init__(width, height, title)
        self.box_list = None

    def start_box_grid(self):
        """ Set up snowfall and initialize variables. """
        self.box_list = []
        
        for row in range(6):
            # Loop for each column
            for column in range(12):
                b = Box(20, 20)  # make new box
                # Calculate our location
                b.x = column * COLUMN_SPACING + LEFT_MARGIN
                b.y = row * ROW_SPACING + BOTTOM_MARGIN   
                self.box_list.append(b)
        
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        for b in self.box_list:
            b.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        for b in self.box_list:
            b.update(delta_time)


def main():
    window = MyGame(SCRN_WIDTH, SCRN_HEIGHT, TITLE)
    window.start_box_grid()
    arcade.run()


# -- MAIN BODY --

if __name__ == "__main__":
    main()
