# @Author:srattigan
# @Date:2021-02-01 13:38:29
# @LastModifiedBy:srattigan
# @Last Modified time:2021-02-01 13:38:29

import random as r
import arcade


def rand_tup(lo, hi, num):
    t = []
    for i in range(num):
        t.append(r.randint(lo, hi))
    return tuple(t)


class Box:
    def __init__(self, w=10, h=10):
        self.width = w
        self.height = h
        self.color = rand_tup(30, 200, 3)
        self.x = 0
        self.y = 0

    def __repr__(self):
        return "Box"

    def draw(self):
        arcade.draw_rectangle_filled(self.x,
                                     self.y,
                                     self.width,
                                     self.height,
                                     self.color)

    def update(self, delta_time):
        self.color = rand_tup(30, 200, 3)
