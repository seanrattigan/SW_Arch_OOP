# create a simple bullet class here

import arcade
from settings import *


class Bullet(arcade.Sprite):
    def __init__(self, center_x, bottom, owner=None):
        arcade.play_sound(GUN_SOUND)
        super().__init__(BULLET_IMG, SPRITE_SCALING_LASER)
        self.angle = -90
        self.change_y = -BULLET_SPEED  # change_y is a property inherited from parent
        self.center_x = center_x  # from origin
        self.top = bottom    # from origin
        self.owner = owner

    def update(self):
        if self.top < 0:
            self.kill()
        self.center_y += self.change_y
        




# bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

