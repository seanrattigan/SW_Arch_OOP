# create the player class here, but:
# the player can only move left and right using the
# left-arrow and right-arrow keys.
# the player can shoot using the up arrow

# After you get init done, and movement, do this
# - give the player a score
# - give the bullet an ID linked to the player

import arcade
from bullet import Bullet

# one way
class Player(arcade.Sprite):
    
    def __init__(self):
        # cal super
        self.bullet_list = arcade.SpriteList
    
    def shoot(self):
        self.bullet_list.append(Bullet(self.center_x, self.top))


# another way
class Player(arcade.Sprite):
    
    def __init__(self):
        # cal super
        pass

    def shoot(self):
        return(Bullet(self.center_x, self.top, self))
