# @Author:srattigan
# @Date:2021-02-04 11:06:13
# @LastModifiedBy:srattigan
# @Last Modified time:2021-02-04 11:18:59

from settings import *
import random
import arcade

default_img = ":resources:images/items/coinGold.png"


class Coin(arcade.Sprite):
    """Emulates a coin

    Args:
        arcade (): inherits from arcade.Sprite class
    """
    def __init__(self, img=default_img):
        super().__init__(img, SPRITE_SCALING_COIN)
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT)
