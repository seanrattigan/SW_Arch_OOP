# @Author:srattigan
# @Date:2021-02-01 12:13:01
# @LastModifiedBy:srattigan
# @Last Modified time:2021-02-01 12:13:01

# Library imports
import arcade

COLUMN_SPACING = 40
ROW_SPACING = 40
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

# Open the window and set the background
arcade.open_window(600, 400, "Grid of boxes")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Loop for each row
for row in range(6):
    # Loop for each column
    for column in range(12):
        # Calculate our location
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        # Draw the item
        arcade.draw_rectangle_filled(x, y, 20, 20, arcade.color.RED)

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()