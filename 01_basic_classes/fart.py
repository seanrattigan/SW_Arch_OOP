# model a Fart class

class Fart:
    """
    Models a Fart
    """
    def __init__(self, dur, pung):
        """Constructor for Fart class

        Returns:
             Fart object
        """
        self.duration = dur
        self.color = (255, 0, 100)
        self.pungency = pung

    def __str__(self):
        """A str representation of the Fart class

        Returns:
            [str]: A description of the internals of the fart
        """
        return f"Fart with color {self.color}, pungency {self.pungency} and
        lasting {self.duration} seconds"

    def effect(self):
        """The effectiveness of a fart to clear a room

        Returns:
            float: the strength of the fart on those nearby
        """
        return self.duration * self.pungency * 100

    def set_color(self, col):
        """Sets the color of the Fart

        Args:
            col (tuple of int): An rgb color
        """
        self.color = col

    def spectral_effect(self):
        r = self.color[0] * self.pungency
        g = self.color[1] * self.pungency
        b = self.color[2] * self.pungency
        return r + g + b


f1 = Fart(3, 0.478)
print(f1)
print("Spectral", f1.spectral_effect())
f1.set_color((0, 255, 0))
print(f1)
print("Effect", f1.effect())
print("Spectral", f1.spectral_effect())
