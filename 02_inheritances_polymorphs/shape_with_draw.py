# @Author:srattigan
# @Date:2020-12-17 19:48:45
# @LastModifiedBy:srattigan
# @Last Modified time:2020-12-17 19:48:45
import turtle
from shape import Square, Triangle

# this exercise will demonstrate inheritance that is
# both multilevel and hierarchical


# create children of the Square and Triangle classes
# and give the children the ability to be drawn

class TriangleReal(Triangle):
    """A Triangle that can be drawn
    """
    def __init__(self, side):
        super().__init__(side)
        self.pos = (200, 200)

    def draw(self):
        tri = turtle.Turtle()
        tri.screen.colormode(255)
        tri.pencolor(self.color)
        tri.pensize(5)
        for i in range(3):
            tri.forward(self.side)
            tri.right(120)
        turtle.done()


new_tri = TriangleReal(300)
new_tri.color = (255, 0, 0)
print(new_tri)
print(new_tri.area())
print(new_tri.perimeter())
new_tri.draw()
