# @Author:srattigan
# @Date:2021-01-14 11:33:20
# @LastModifiedBy:srattigan
# @Last Modified time:2021-01-14 11:33:20

import math
import arcade
import random as r

# globals
colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0)
}

# Constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def validate_color(col):
    # if type is tuple
    #   if len is 3
    #     if each is int
    #         it's true
    # otherwise false
    pass


class Rectangle:
    """Models a rectangle
    """
    def __init__(self, width, height, color=(0, 255, 0)):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
            color (tuple, optional): an rgb color. Defaults to (0, 255, 0).
        """
        # make sure valid nums, color
        self.height = height
        self.width = width
        self.color = color

    def __repr__(self):
        """[summary]

        Returns:
            str: a string rep of a rectangle
        """
        return f"Rect: w={self.width}; h={self.height}; col={self.color}"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def set_color(self, col):
        # MAKE SURE VALID COLOR
        self.color = col

    def draw(self):
        arcade.draw_rectangle_filled(r.randrange(100, 200),  # x
                                     r.randrange(100, 200),  # y
                                     self.width,
                                     self.height,
                                     self.color)

    def __add__(self, other):
        new_area = self.area() + other.area()
        # square_area = side ** 2
        # side = square_area
        side = math.sqrt(new_area)  # given a square with area new_area
        return Rectangle(side, side)

    def __sub__(self, other):
        new_area = self.area() - other.area()  # use absolute
        # r1 side is 4, r2 side is 5, what's r1 - r2?
        side = math.sqrt(new_area)
        return Rectangle(side, side)

    def __mul__(self, num):
        new_area = self.area() * num
        side = math.sqrt(new_area)
        return Rectangle(side, side)

    def __truediv__(self, num):
        new_area = self.area() / num
        side = math.sqrt(new_area)
        return Rectangle(side, side)

    def __eq__(self, other):  # ==
        return self.area() == other.area()

    def __ne__(self, other):  # !=
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()



    


if __name__ == "__main__":
    r1 = Rectangle(3,5)
    r2 = Rectangle("dog", "cat")
    r3 = Rectangle(-33, "88i")
    r4 = r3 - r2
    r1.set_color((240, 34, 56))
