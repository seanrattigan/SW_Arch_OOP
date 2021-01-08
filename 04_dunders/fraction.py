# @Author:srattigan
# @Date:2021-01-07 11:12:16
# @LastModifiedBy:srattigan
# @Last Modified time:2021-01-08 10:11:03


def gcd(num, denom):
    result = num % denom
    if result == 0:
        return denom
    elif result == 1:
        return 1
    return gcd(denom, result)

class Fraction:
    """Simulates a Fraction class
    """
    def __init__(self, frac):
        """Constructor for Fraction class

        Args:
            frac (str): str rep of a fraction
        """
        fracrep = frac.split('/')
        try:
            self.numerator = int(fracrep[0])
            self.denominator = int(fracrep[1])
        except TypeError:
            raise TypeError("Must use valid format of fraction")
        self.reduce()

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __float__(self):
        """Converts a Fraction to a float

        Returns:
            float: float of thee Fractions
        """
        return self.numerator / self.denominator
        
    def __invert__(self):
        """Creates and returns a new instance of a Fraction
        which is inverted

        Returns:
            [Fraction]: inverted from the original
        """
        temp = f"{self.denominator}/{self.numerator}"
        return Fraction(temp)

    def reduce(self):
        """A reduction algorithm
        """
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator = self.denominator // common

    def __add__(self, other):
        """Overload the "+" operator for use with Fractions

        Args:
            other (Fraction): Another instance of Fraction
        """
        bottom = self.denominator * other.denominator
        top = self.numerator * other.denominator + other.numerator * self.denominator
        rep = f"{top}/{bottom}"
        return Fraction(rep)

    def __sub__(self, other):
        """Overload the "+" operator for use with Fractions

        Args:
            other (Fraction): Another instance of Fraction
        """
        bottom = self.denominator * other.denominator
        top = self.numerator * other.denominator - other.numerator * self.denominator
        rep = f"{top}/{bottom}"
        return Fraction(rep)

    def __mul__(self, other):
        """Implements operator overloading for the *
        to use with Fractions

        Args:
            other (Fraction): a Fraction instance

        Returns:
            Fraction: a Fraction instance
        """
        top = self.numerator * other.numerator
        bottom = self.denominator * other.denominator
        rep = f"{top}/{bottom}"
        return Fraction(rep)

    def __truediv__(self, other):
        """Implements operator overloading for the /
        to use with Fractions

        Args:
            other (Fraction): a Fraction instance

        Returns:
            Fraction: a Fraction instance
        """
        second = ~other
        return self * second



# a = Fraction('2/16')
# b = Fraction('1/33')
# print(b / a)
# print(a * )
x = Fraction('25/79')
y = Fraction('33/117')
print(y - x)
# f1 = Fraction(1, 2)  # for 1/2
f2 = Fraction('1/2')  # for 1/2
f1 = Fraction('1/4')
f3 = f1 + f2  # 6/8
print(f3)
f4 = f2 - f1  # 2/8
print(f4)
print(float(f2))
print(f1.__float__())
print(~f3)
print(f3)
