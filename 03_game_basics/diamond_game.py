"""
Sprite Collect Coins Moving Down

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_collect_coins_move_down
"""

import random
import arcade
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Moving Down Example"


class Diamond(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        #self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.player_sprite_list = None
        self.diamond_sprite_list = None

        # Set up the player info
        self.player_sprite = None

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.diamond_sprite_list = arcade.SpriteList()

        # Score
        self.score = 0

#        # Set up the player
#        # Character image from kenney.nl
#        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
#        self.player_sprite.center_x = 50
#        self.player_sprite.center_y = 50
#        self.player_sprite_list.append(self.player_sprite)
        self.diamond_factory(10, self.diamond_sprite_list)


    def diamond_factory(self, n, bucket):
        start_x = 50
        start_y = SCREEN_HEIGHT - 50
        x_offset = (SCREEN_WIDTH - 50) / n
        for i in range(n):
            di = Diamond(":resources:images/items/gemBlue.png", SPRITE_SCALING_COIN)
            
            # Position the obj
            di.center_x = start_x
            di.center_y = start_y
            start_x += x_offset
            # Add the obj to the lists
            bucket.append(di)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.diamond_sprite_list.draw()
#        self.player_sprite_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.diamond_sprite_list.update()

#        # Generate a list of all sprites that collided with the player.
#        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
#                                                        self.coin_sprite_list)
#
#        # Loop through each colliding sprite, remove it, and add to the score.
#        for coin in hit_list:
#            coin.remove_from_sprite_lists()
#            self.score += 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()