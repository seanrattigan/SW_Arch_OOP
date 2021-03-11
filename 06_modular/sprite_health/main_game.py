"""
Sprite Hit Points and Health Bars
"""
import random
import arcade
from coin import HealthCoin
from bullet import Bullet
from settings import *


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        # Set up the player info
        self.player_sprite = None
        self.score = 0
        # Don't show the mouse cursor
        self.set_mouse_visible(False)
        # Load sounds are in settings- sorted with associated obj
        arcade.set_background_color(arcade.color.AMAZON)

        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            coin = HealthCoin(COIN_IMG,
                              SPRITE_SCALING_COIN)
            # Position the coin
            coin.set_pos(random.randrange(SCREEN_WIDTH),
                         random.randrange(150, SCREEN_HEIGHT))
            # Add the coin to the lists
            self.coin_list.append(coin)
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        
        # Draw all the sprites.
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        for coin in self.coin_list:
            coin.draw_health_number()
            coin.draw_health_bar()

       # draw a black box at top of screen

        # render the text on top
        arcade.draw_text(f"Score: {self.score}", 10, 20,
                         arcade.color.WHITE, 14,
                         font_name='Arial')


    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        bullet = Bullet(self.player_sprite.center_x, self.player_sprite.top)
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        self.bullet_list.update()  # using default update for Sprite

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.kill()

            # For every coin we hit, process
            for coin in hit_list:
                # Make sure this is the right type of class
                if not isinstance(coin, HealthCoin):
                    raise TypeError("List contents must be all coins")
                self.score += coin.hit(2)  # bullet.owner.score += coin.hit(2)


def main():
    """ Main Program """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
