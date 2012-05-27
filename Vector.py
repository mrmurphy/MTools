# This is a class to make vector math, and working with vectors easy.
# Written by Murphy Randle, 2012: murphyrandle@gmail.com
# Heavily referenced from: http://www.math.okstate.edu/~ullrich/PyPlug/
import math


class Vector(object):
    def __init__(self, *indata):
        # This is to check if the args are a list, or just values.
        if (len(indata) > 0):
            if (type(indata[0]) == type([])) or \
               (type(indata[0]) == type(())):
                indata = indata[0]
        self.data = list(indata)
        self.setup()

    def setup(self):
        self.magnitude = math.sqrt(sum([math.pow(x, 2) for x in self.data]))

        # If the vector has greater than three dimensions, break it up.
        if (len(self.data) >= 3):
            self.x = self.data[0]
            self.y = self.data[1]
            self.z = self.data[2]
            if (len(self.data) == 4):
                self.h = self.data[3]

    def __repr__(self):
        return self.__str__()
        # return repr(self.data)

    def __add__(self, other):
        return Vector([self.data[i] + other.data[i] for i in range(len(self.data))])

    def __sub__(self, other):
        return Vector([self.data[i] - other.data[i] for i in range(len(self.data))])

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __mul__(self, other):
        return Vector([x * other for x in self.data])

    def __rmul__(self, other):
        return Vector([x * other for x in self.data])

    def __div__(self, other):
        if (other == 0):
            other = 1
        return Vector([(x / other) for x in self.data])

    def __eq__(self, other):
        if (len(self.data) != len(other.data)):
            return False
        for i in range(len(self.data)):
            if (self.data[i] != other.data[i]):
                return False
        return True

    def __str__(self):
        result = " ".join([str(x).center(4) for x in self.data])
        return result

    def xSet(self, val):
        self.data[0] = val
        self.setup()

    def ySet(self, val):
        self.data[1] = val
        self.setup()

    def zSet(self, val):
        self.data[2] = val
        self.setup()

    def dot(self, other):
        # This will provide the dot product of the vector.
        result = []
        for i in range(len(self.data)):
            result.append(self.data[i] * other.data[i])
        return sum(result)

    def cross(self, other):
        # This should only be used with a 3 dimensional vector.
        # Returns the vector result of the cross product.
        newX = (self.y * other.z) - (self.z * other.y)
        newY = (self.z * other.x) - (self.x * other.z)
        newZ = (self.x * other.y) - (self.y * other.x)
        return Vector(newX, newY, newZ)

    def normalize(self):
        mag = self.magnitude
        self.xSet(float(self.x / mag))
        self.ySet(float(self.y / mag))
        self.zSet(float(self.z / mag))
        return self

# Test cases:
if __name__ == '__main__':
    x = Vector(1, 2, 3)
    assert round(x.magnitude) == 4.0
    x = x * 2
    assert x == Vector(2, 4, 6)
    x.normalize()
    print (x)
    print((x.magnitude))
