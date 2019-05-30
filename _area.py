# We need this module for some of the formulas
import math

# Area of a Square
def areaSqr(side):
    return side**2

# Area of a Rectangle
def areaRect(width, height):
    return width * height

# Area of a Triangle
def areaTri(base, height):
    return (base * height) / 2

# Area of a Circle
def areaCirc(radius):
    return math.pi * radius**2

# Area of Ellipse
def areaEll(axis1, axis2):
    return math.pi * axis1 * axis2

# Area of a Trapezoid
def areaTrap(base1, base2, height):
    return ((base1 + base2) / 2) * height

# Area of any Polygon
def areaPoly(side, sideCount):
    return (side**2 * sideCount) / (4 * math.tan(180 / sideCount))
