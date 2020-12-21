import math

# this example has several features;
# - hierarchical inheritance
# - a class variable as distinct from instance variables
# - a generic __str__ method using this class dict
# - a generic perimeter method
# - raising an error for a method not implemented in the Parent
# - polymorphism


class Shape:
    """An abstract Shape class
    While we may not actually instantiate a "shape" I've tried to
    describe what a shape of 'n' sides might be.
    Any shape we make will in practise have some value for the
    number of sides."""
    shape_family = {0: "Nothing",
                    1: "Dot",
                    2: "Line",
                    3: "Triangle",
                    4: "Square",
                    5: "Pentagon",
                    6: "Hexagon"}

    def __init__(self, side):
        self.side = side
        self.num_sides = 0
        self.color = (0, 0, 0)

    def __str__(self):
        shape_type = self.shape_family[self.num_sides]
        return f"A {shape_type} with {self.num_sides} sides of len {self.side} and color {self.color}"

    def perimeter(self):
        return self.side * self.num_sides

    def area(self):
        raise NotImplementedError("Not implemented for this *abstract* class")


class Triangle(Shape):
    def __init__(self, side):
        """Constructor
        """
        super().__init__(side)
        self.num_sides = 3
        self.color = (0, 255, 0)

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2


class Square(Shape):  # red
    def __init__(self, side):
        """Constructor
        """
        super().__init__(side)
        self.num_sides = 4
        self.color = (255, 0, 0)

    def area(self):
        return self.side ** 2


class Pentagon(Shape):  # blue
    pass


class Hexagon(Shape):  # yellow
    pass


class Circle:
    def __init__(self, rad):
        self.radius = rad
        self.color = (255, 255, 255)
    
    def perimeter(self):
        return math.pi * 2 * self.radius

    def area(self):
        return math.pi * self.radius ** 2


# this test code MUST be run conditionally if the module/file
# is to be imported into another file
if __name__ == "__main__":
    shape_bucket = []
    t1 = Triangle(5)
    shape_bucket.append(t1)
    s1 = Square(6)
    shape_bucket.append(s1)
    c1 = Circle(4)
    shape_bucket.append(c1)
    for shape in shape_bucket:
        print(shape)
        print("Perimeter is", shape.perimeter())
        print("Area is", shape.area())
