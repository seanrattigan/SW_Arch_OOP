# @Author:srattigan
# @Date:2021-02-12 09:23:31
# @LastModifiedBy:srattigan
# @Last Modified time:2021-02-12 18:22:26
import arcade
from settings import *


keysets = [
    [arcade.key.LEFT,
     arcade.key.UP,
     arcade.key.RIGHT,
     arcade.key.DOWN],
    [arcade.key.A,
     arcade.key.W,
     arcade.key.D,
     arcade.key.S],
    [arcade.key.J,
     arcade.key.I,
     arcade.key.L,
     arcade.key.K]
]

p_images = [":resources:images/animated_characters/female_person/femalePerson_idle.png",
            ":resources:images/animated_characters/male_person/malePerson_idle.png",
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"]

positions = [[50, 50],
             [100, 50],
             [150, 50]]

i = arcade.Sprite()


class Player(arcade.Sprite):
    """A Player with movement up down left right

    Relies on several settings:
    - SPRITE_SCALING
    - MOVEMENT_SPEED = 5
    - SPRITE_SCALING
    - SCREEN_WIDTH
    - SCREEN_HEIGHT
    - player_img (a default image for the player)
    """
    player_num = 0  # formerly called counter

    def __init__(self, img=None):
        super().__init__(p_images[Player.player_num], SPRITE_SCALING)
        self.id = self.player_num + 1
        self.center_x = positions[Player.player_num][0]
        self.center_y = positions[Player.player_num][1]
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        # keys are in order of L, U, R, D
        self.keys = keysets[Player.player_num]
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        Player.player_num += 1

    def __repr__(self):
        return f"Player {self.id} @pos({self.center_x},{self.center_y} using {self.keys}"

    def key_handler(self, key, pressed):
        """Called if a key belongs to the Player instance
        if the key was pressed, the pressed var is True
        but if released, the pressed var is False

        Args:
            key (int): an int corresponding to a keyboard key
            pressed (bool): True for pressed, False for released
        """
        # print("Key handler called")
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

    def set_pos(self, x, y):
        """Setter method for Player

        Args:
            x (num): the x-pos of the Player
            y (num): the y-pos of the Player
        """
        self.center_x = x
        self.center_y = y

    def update(self):
        """ Move the player
        Monitors the status of key_pressed (left, right, up, down)
        and adjusts position accordingly
        """
        # Move player.
        self.change_x = 0
        self.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.change_y = self.speed
        elif self.down_pressed and not self.up_pressed:
            self.change_y = -self.speed
        if self.left_pressed and not self.right_pressed:
            self.change_x = -self.speed
        elif self.right_pressed and not self.left_pressed:
            self.change_x = self.speed

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


if __name__ == "__main__":
    player_1 = Player()
    player_2 = Player()
    player_3 = Player()
    print(player_1.__repr__())  # sr could be
    print(player_2)  # Player 2 [3] 3876    
    print(player_3)
