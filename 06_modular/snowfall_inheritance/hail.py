from snowflake import Snowflake
import arcade
import random


class Hail(Snowflake):
    def __init__(self):
        super().__init__()
        self.size = random.randrange(4, 10)
        self.color = arcade.color.YELLOW
        self.speed = -random.randrange(20, 40)

    # def update(self, delta_time):
    #     pass
    # have it drift down,
    # change the angle by 10 each time
    # WHEN the EDGE of the circle hits the bottom
    # make it BOUNCE
    # have them bounce back when they hit the top/ sides as well :D
