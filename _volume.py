# We need this module for some of the formulas
import math

# Volume of a Cube
def volCube(edge):
    return edge**3

# Volume of a Rectangular Prism
def volRect(width, length, height):
    return width * length * height

# Volume of a Triangular Prism
def volTri(base1, base2, base3, height):
    return 1/4 * height * math.sqrt( -base1**4 + 2 * (base1*base2)**2 + 2 * (base1*base3)**2 - base2**4 + 2 * (base2*base3)**2 - base3**4 )

# Volume of a Right Rectangular Pyramid
def volPyr(length, width, height):
    return (length * width * height) * 1/3

# Volume of a Sphere
def volSph(radius):
    return 4/3 * math.pi * radius**3

# Volume of a Right Cylinder
def volCyl(radius, height):
    return math.pi * radius**2 * height

# Volume of a Right Circular Cone
def volCone(radius, height):
    return math.pi * radius**2 * (height / 3)
