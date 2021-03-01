# move the SpriteWithHealth in here as a new HealthCoin class

import arcade
from settings import *


class HealthCoin(arcade.Sprite):
    """ Sprite with hit points """

    def __init__(self, image, scale, max_health=6):
        super().__init__(image, scale)
        self.worth = 4
        # Add extra attributes for health
        self.max_health = max_health
        self.cur_health = max_health

    def set_pos(self, x, y):
        self.center_x = x
        self.center_y = y

    def hit(self, pow=1):
        self.cur_health -= pow
        if self.cur_health <= 1:
            arcade.play_sound(COIN_DEAD_SND)
            points = self.worth
            self.kill()
            return points
        arcade.play_sound(COIN_HIT_SND)
        return 0

    def draw_health_number(self):
        """ Draw how many hit points we have """

        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                         start_x=self.center_x + HEALTH_NUMBER_OFFSET_X,
                         start_y=self.center_y + HEALTH_NUMBER_OFFSET_Y,
                         font_size=12,
                         color=arcade.color.WHITE)

    def draw_health_bar(self):
        """ Draw the health bar """

        # Draw the 'unhealthy' background
        if self.cur_health < self.max_health:
            arcade.draw_rectangle_filled(
                center_x=self.center_x,
                center_y=self.center_y + HEALTHBAR_OFFSET_Y,
                width=HEALTHBAR_WIDTH,
                height=3,
                color=arcade.color.RED)

        # Calculate width based on health
        health_width = HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(
            center_x=self.center_x - 0.5 * (HEALTHBAR_WIDTH - health_width),
            center_y=self.center_y - 10,
            width=health_width,
            height=HEALTHBAR_HEIGHT,
            color=arcade.color.GREEN)
