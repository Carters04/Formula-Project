# We need this module for some of the formulas
import math

# Perimeter of a Square
def perSqr(side):
    return side * 4

# Perimeter of a Rectangle
def perRect(width, height):
    return (width * 2) + (height * 2)

# Perimeter of any Polygon
def perPoly(side, sideCount):
    return side * sideCount
