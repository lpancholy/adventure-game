import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        distance = math.sqrt((self.x + point.x)**2.0 + (self.y + point.y)**2.0)
        return distance

    def __repr__(self):
        return("(%d, %d)" % (self.x, self.y))
