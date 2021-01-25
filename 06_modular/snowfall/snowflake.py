# @Author:srattigan
# @Date:2021-01-25 10:01:31
# @LastModifiedBy:srattigan
# @Last Modified time:2021-01-25 10:01:31

import random
from settings import *


class Snowflake:
    """
    Each instance of this class represents a single snowflake.
    Based on drawing filled-circles.
    """

    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_pos(self):
        # Reset flake to random position above screen
        self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.x = random.randrange(SCREEN_WIDTH)
