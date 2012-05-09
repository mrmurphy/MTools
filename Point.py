# A class to make working with points very easy.
from Vector import Vector

class Point(Vector):
    def __init__(self, x, y, z):
        super(Point, self).__init__(x, y, z, 1)