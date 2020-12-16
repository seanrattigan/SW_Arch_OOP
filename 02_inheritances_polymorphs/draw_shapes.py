
import turtle

# quick tutorial on using turtle:
# https://www.tutorialspoint.com/turtle-graphics-using-python
# comprehensive documentation is located at:
# https://docs.python.org/3/library/turtle.html


def draw_star():
    star = turtle.Turtle()
    for i in range(100):
        star.forward(100)
        star.right(144)
    turtle.done()


def draw_square():
    square = turtle.Turtle()
    square.screen.colormode(255)
    square.pencolor((255, 0, 0))
    square.pensize(5)
    # write code to draw square here
    turtle.done()


# draw_square()  # call the func

# create the function for this
# do the same for Triangle


# Note: the degrees to turn as a function of num_sides
