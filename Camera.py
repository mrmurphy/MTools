# A quick camera class to store the values needed to represent a
# camera in this pipeline.
from Vector import Vector

class Camera(object):
    def __init__(self):
       self.e = Vector(0, 0, 0)
       self.g = Vector(0, 0, -1)
       self.t = Vector(0, 1, 0)
       self.n = -1
       self.f = -10
       self.angle = 70

    def calc(self):
       self.w = -1 * self.g
       self.u = self.t.cross(self.w)
       self.u = self.u / self.u.magnitude
       self.v = self.w.cross(self.u)

    def eSet(self, x, y, z):
        self.e = Vector(x, y, z)
        self.calc()

    def gSet(self, x, y, z):
        self.g = Vector(x, y, z)
        self.calc()

    def tSet(self, x, y, z):
        self.t = Vector(x, y, z)
        self.calc()

    def nSet(self, val):
        self.n = val
        self.calc()

    def fSet(self, val):
        self.f = val
        self.calc()

    def angleSet(self, val):
        self.angle = val
        self.calc()
