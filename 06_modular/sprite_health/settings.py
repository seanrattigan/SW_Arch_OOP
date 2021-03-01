# @Author:srattigan
# @Date:2021-02-25 14:10:09
# @LastModifiedBy:srattigan
# @Last Modified time:2021-02-25 14:10:09
import arcade

# Settings for screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hit Points and Health Bars"

#Settings for Player
MOVEMENT_SPEED = 5
SPRITE_SCALING_PLAYER = 0.5
player_img = ":resources:images/animated_characters/female_person/femalePerson_idle.png"

# Settings for Bullet
GUN_SOUND = arcade.load_sound(":resources:sounds/hurt5.wav")
BULLET_IMG = ":resources:images/space_shooter/laserBlue01.png"
SPRITE_SCALING_LASER = 0.8
BULLET_SPEED = 10

# Settings for Coin
COIN_IMG = ":resources:images/items/coinGold.png"
HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25

SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50
COIN_HIT_SND = arcade.load_sound(":resources:sounds/hit4.wav")
COIN_DEAD_SND = arcade.load_sound(":resources:sounds/hit5.wav")