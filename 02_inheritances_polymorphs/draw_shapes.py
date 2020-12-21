# @Author:srattigan
# @Date:2020-12-21 09:26:42
# @LastModifiedBy:srattigan
# @Last Modified time:2020-12-21 09:26:42

import turtle

# quick tutorial on using turtle:
# https://www.tutorialspoint.com/turtle-graphics-using-python
# comprehensive documentation is located at:
# https://docs.python.org/3/library/turtle.html


def draw_star():
    star = turtle.Turtle()
    star.screen.colormode(255)
    star.pencolor((240, 100, 210))
    star.pensize(10)
    star.left(45)
    for i in range(5):
        star.forward(200)
        star.right(144)
    turtle.done()


def draw_star_fill():
    star = turtle.Turtle()
    star.screen.colormode(255)
    star.pencolor((240, 100, 210))
    star.fillcolor((240, 100, 210))
    star.begin_fill()
    for i in range(5):
        star.forward(200)
        star.right(144)
    star.end_fill()
    turtle.done()



def draw_square():
    print("Square Called")
    square = turtle.Turtle()
    square.screen.colormode(255)
    square.pencolor((255, 0, 0))
    square.pensize(5)
    # write code to draw square here
    turtle.done()


# draw_star()
draw_star_fill()
# draw_square()
# draw_square()  # call the func

# create the function for this
# do the same for Triangle


# Note: the degrees to turn as a function of num_sides
