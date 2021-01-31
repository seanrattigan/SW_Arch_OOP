# @Author:srattigan
# @Date:2021-01-25 10:01:31
# @LastModifiedBy:srattigan
# @Last Modified time:2021-01-25 10:44:23

import random
import math
import arcade
from settings import *


class Snowflake:
    """
    Each instance of this class represents a single snowflake.
    Based on drawing filled-circles.
    """

    def __init__(self):
        """Constructor for class Snowflake
        """
        self.x = 0
        self.y = 0
        self.size = random.randrange(4)
        self.speed = random.randrange(20, 40)
        self.angle = random.uniform(math.pi, math.pi * 2)

    def set_new_pos(self):
        # Reset flake to random position above screen
        self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
        self.x = random.randrange(SCREEN_WIDTH)

    def draw(self):
        arcade.draw_circle_filled(self.x,
                                  self.y,
                                  self.size,
                                  arcade.color.WHITE)

    def update(self, delta_time):
        self.y -= self.speed * delta_time
        if self.y < 0:
            self.set_new_pos()
        self.x += self.speed * math.cos(self.angle) * delta_time
        self.angle += 1 * delta_time


if __name__ == "__main__":
    print("Snowflake class file")
