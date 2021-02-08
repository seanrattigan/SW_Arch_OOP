# @Author:srattigan
# @Date:2021-02-04 11:29:41
# @LastModifiedBy:srattigan
# @Last Modified time:2021-02-04 12:54:40

from settings import *
import arcade

player_img = ":resources:images/animated_characters/female_person/femalePerson_idle.png"


class Player(arcade.Sprite):
    def __init__(self, img=player_img):
        super().__init__(img, SPRITE_SCALING_PLAYER)
        self.center_x = 50
        self.center_y = 50
