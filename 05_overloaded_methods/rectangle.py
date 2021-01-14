
colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0)
}

class Rectangle:
    def __init__(self, width, height, color=(0, 255, 0)):
        self.height = height
        self.width = width
        self.color = color

    def __repr__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def set_color(self):
        pass

    def draw(self):
        pass
    
    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, num):
        pass

    def __truediv__(self, num):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass



    



r1 = Rectangle(3,5)
r2 = Rectangle("dog", "cat")
r3 = Rectangle(-33, "88i")
r4 = r3 - r2