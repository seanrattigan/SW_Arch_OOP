import math

# this example shows the use of private attributes
# private instance vars cannot be accessed directly
# and must be accessed/modified via getter/setter methods


class Sphere:
    """Simulates a sphere
    """
    def __init__(self, radius):
        """
        (num) -> obj
        Constructor
        """
        self.__radius = radius
        self.__color = (255, 0, 0)  # rgb

    def set_radius(self, rad):
        """
        (num) -> None
        Sets the radius of the sphere
        """
        self.__radius = rad

    def get_radius(self):
        """
        (None) -> num
        Gets the radius of the sphere
        """
        return self.__radius

    def set_color(self, col):
        """
        (tuple of int) -> None
        Sets the color of the sphere
        """
        self.__color = col

    def get_color(self):
        """
        (None) -> tuple of int
        Gets the color of the sphere
        """
        return self.__color

    def area(self):
        """Calculates surface area of sphere

        Returns:
            float: surface area of sphere object
        """
        return 4 * math.pi * self.get_radius() ** 2
  
    def volume(self):
        """Calculates volume of the sphere

        Returns:
            float: volume of sphere object
        """
        return 4 / 3 * math.pi * self.get_radius() ** 3


# short test code
s1 = Sphere(5)
print(s1.get_color())
s1.set_radius(7.5)
print(s1.area())
print(s1.volume())
