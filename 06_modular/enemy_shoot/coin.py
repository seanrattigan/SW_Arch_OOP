import random
import arcade
from settings import *
from bullet import Bullet

class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0
        self.bullet_list = arcade.SpriteList()

    def update(self):
        num = random.randrange(100)
        if num == 99:
            self.bullet_list.append(Bullet(self.center_x, self.bottom))
            # print("Bullet fired")
        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y
        small_dev = random.randrange(-100, 100) / 1000
        # If we are out-of-bounds, then 'bounce'
        dev = 1 + small_dev
        if self.left < 0:
            self.change_x *= -dev

        if self.right > SCREEN_WIDTH:
            self.change_x *= -dev

        if self.bottom < 0:
            self.change_y *= -dev

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -dev
