# We need this module for some of the formulas
import math

# Surface Area of a Cube
def surfCube(edge):
    return 6 * edge**2

# Surface Area of a Rectangular Prism
def surfRect(width, length, height):
    return ((width * length) + (width * height) + (length * height)) * 2

# Surface Area of a Sphere
def surfSph(radius):
    return 4 * math.pi * radius**2
