
"""
Better Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
This is slightly better than sprite_move_keyboard.py example
in how it works, but also slightly more complex.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard_better
"""

import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Better Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5

player_img = ":resources:images/animated_characters/female_person/femalePerson_idle.png"


class Player(arcade.Sprite):
    def __init__(self, img=player_img):
        super().__init__(img, SPRITE_SCALING)
        self.center_x = 50
        self.center_y = 50
        self.change_x = 0
        self.change_y = 0
        # keys are in order of L, U, R, D
        self.keys = [arcade.key.LEFT,
                     arcade.key.UP,
                     arcade.key.RIGHT,
                     arcade.key.DOWN]
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def key_handler(self, key, pressed):
        """Called if a key belongs to the Player instance
        if the key was pressed, the pressed var is True
        but if reeased, the pressed var is False

        Args:
            key (int): an int corresponding to a keyboard key
            pressed (bool): True for pressed, False for released
        """
        if key == self.keys[0]:
            self.left_pressed = pressed
        if key == self.keys[1]:
            self.up_pressed = pressed
        if key == self.keys[2]:
            self.right_pressed = pressed
        if key == self.keys[3]:
            self.down_pressed = pressed

    def set_keys(self, key_list):
        """Sets the keys for a player instance

        Args:
            key_list (list of four ints): Each int maps to a keyboard
        >>> player2 = Player()
        >>> player2.set_keys([arcade.key.A,
                              arcade.key.W,
                              arcade.key.D,
                              arcade.key.S])
        """
        self.keys = key_list

    def update(self):
        """ Move the player 
        Monitors the status of key_pressed (left, right, up, down)
        and adjusts position accordingly
        """
        # Move player.
        self.change_x = 0
        self.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.change_x = MOVEMENT_SPEED
        
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds of screen
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


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
        for player in self.player_list:
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