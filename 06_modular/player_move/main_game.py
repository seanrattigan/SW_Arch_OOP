
"""
Better Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
This is slightly better than sprite_move_keyboard.py example
in how it works, but also slightly more complex.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from 
the command line with:
python -m arcade.examples.sprite_move_keyboard_better
"""

import arcade
from player import Player
from settings import *


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the players
        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.player_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Call update to move the sprite
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. 
        For each player, the method will now check if the key
        belongs to a player, and if it does, call the key_handler
        to let the instance know a key belonging to it was pressed
        """
        # if key pressed is the letter "P", print player(s)
        for player in self.player_list:
            if key == arcade.key.P:  # for test and debug
                print(player)
            if key in player.keys:
                player.key_handler(key, True)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. 
        For each player, the method will now check if the key
        belongs to a player, and if it does, call the key_handler
        to let the instance know a key belonging to it was released
        """
        for player in self.player_list:
            if key in player.keys:
                player.key_handler(key, False)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()