# We need this module for some of the formulas
import math

# Quadratic Formula
def quad(a, b, c):
    ans1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
    ans2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a

    if ans1 == ans2:
        ans = [ans1]
        return ans
    else:
        ans = [ans1, ans2]
        return ans

# Distance Formula
def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Slope Forumula
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Midpoint Forumla
def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    ans = [x, y]
    return ans

# Sine Formula
def sin(opposite, hypotenuse):
    return opposite / hypotenuse

# Cosine Formula
def cosin(adjacent, hypotenuse):
    return adjacent / hypotenuse

# Tangent Formula
def tan(opposite, adjacent):
    return opposite / adjacent
