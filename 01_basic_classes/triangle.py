# imports
import math
import random

# globals
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# class or function
class Triangle:
    def __init__(self, side):
        """Constuctor for an equilateral triangle

        Args:
            side (num): A length in cm
        """
        self.num_sides = 3
        self.side_len = side
        self.color = (0, 255, 0)

    def perimeter(self):
        """Calculates the perimeter of the triangle

        Returns:
            float: the perimeter of the object
        """
        return self.side_len * 3.0

    def area(self):
        """Calculates the area of the triangle

        Returns:
            float: the area of the triangle
        """
        return math.sqrt(3) / 4 * self.side_len ** 2

    def __str__(self):
        s = self.side_len
        c = self.color
        return f"Equal sided Triangle with side len {s}, color {c}"


# how to test one instance?
# t1 = Triangle(5)
# print(t1)
# print("Perimeter", t1.perimeter())
# print("Area", t1.area())

# how to test many?
bucket = []
for t in range(3):
    tri = Triangle(random.randrange(10))
    bucket.append(tri)
# print them all
for t in bucket:
    print(f"\n{t}")
    print(f"Area is {t.area()}")
    print(f"Perim is {t.perimeter()}")
