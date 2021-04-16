# @Author:srattigan
# @Date:2021-01-25 09:55:57
# @LastModifiedBy:srattigan
# @Last Modified time:2021-01-25 10:00:49

# -- IMPORTS --
import random
import math
import arcade
from settings import *
# from snowflake import Snowflake
from hail import Hail

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
        self.snowflake_list = None

    def start_snowfall(self):
        """ Set up snowfall and initialize variables. """
        self.snowflake_list = []
        for i in range(NUM_FLAKES):
            snowflake = Hail()
            snowflake.set_new_pos()
            self.snowflake_list.append(snowflake)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        for snowflake in self.snowflake_list:
            snowflake.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        for snowflake in self.snowflake_list:
            snowflake.update(delta_time)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_snowfall()
    arcade.run()


# -- MAIN BODY --

if __name__ == "__main__":
    main()
