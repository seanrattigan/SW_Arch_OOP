
# a basic class example with inheritance

class Rectangle:
    """Emulates a rectangle"""
    def __init__(self, length, width):
        """
        Constructor
        """
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        perim = 2 * (self.width + self.length)
        return perim
    
    def __str__(self):
        return f"Rectangle {self.length} long and {self.width} wide"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


if __name__ == "__main__":
    rect_1 = Rectangle(3, 7.0)
    print(f"Rectangle Area: {rect_1.area()}")
    print(f"Rectangle Perim: {rect_1.perimeter()}")

    sqr_1 = Square(5)
    print(f"Rectangle Area: {sqr_1.area()}")
    print(f"Rectangle Perim: {sqr_1.perimeter()}")
