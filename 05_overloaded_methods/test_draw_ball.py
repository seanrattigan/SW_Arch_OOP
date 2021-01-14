# @Author:srattigan
# @Date:2021-01-12 22:14:38
# @LastModifiedBy:srattigan
# @Last Modified time:2021-01-13 10:33:24

import arcade
import random
from rectangle import Rectangle

# Set constants for the screen size
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Test My Rectangles"

bucket = [Rectangle(50, 5), Rectangle(10, 44)]


def draw_rectangles(rectangle_array):
    # Open the window. Set the window title and dimensions
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Set the background color
    arcade.set_background_color(arcade.color.BLACK)

    # Clear screen and start render process
    arcade.start_render()

    # --- Drawing Commands Will Go Here ---

    # Draw the Rectangle
    for b in Rectangle_array:
        b.draw()

    # Finish drawing and display the result
    arcade.finish_render()

    # Keep the window open until the user hits the 'close' button
    arcade.run()


if __name__ == "__main__":
    draw_rectangles(bucket)
