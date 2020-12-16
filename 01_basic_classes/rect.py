
# a basic class example

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

