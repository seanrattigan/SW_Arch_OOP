# @Author:srattigan
# @Date:2020-12-18 10:17:41
# @LastModifiedBy:srattigan
# @Last Modified time:2020-12-21 09:51:46
from shape import Shape
import turtle


class ShapeReal(Shape):
    """A class to model shapes with any number of sides above three
    and facilitate drawing that shape and calculating the perimeter.
    The area in the parent is unimplemented.
    <do stuff> if <condition>
    Args:
        Shape ([type]): [description]
    """
    def __init__(self, side):
        super().__init__(side)

    def draw(self, fill=False):
        shape = turtle.Turtle()
        shape.screen.colormode(255)
        shape.pencolor(self.color)
        shape.fillcolor(self.color)
        if fill:
            shape.begin_fill()
        for i in range(self.num_sides):
            shape.forward(self.side)
            shape.right(360/self.num_sides)
        if fill:
            shape.end_fill()
        turtle.done()


class TriangleReal(ShapeReal):
    def __init__(self, side):
        super().__init__(side)
        self.num_sides = 3
        self.color = (0, 255, 0)


class SquareReal(ShapeReal):
    def __init__(self, side):
        super().__init__(side)
        self.num_sides = 4
        self.color = (255, 0, 0)


tri_1 = SquareReal(200)
# tri_1.color = (0,0,255)
print(tri_1)
# tri_1.draw()
tri_1.draw()
