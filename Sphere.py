# A simple representation of a sphere.
from MTools.Vector import Vector


class Sphere(object):
    def __init__(self, center, radius, color=[0xff, 0xff, 0xff, 0xff]):
        self.center = Vector(center)
        self.radius = radius
        self.color = color
