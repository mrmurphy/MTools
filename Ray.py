# A simple definition of an array.
# Designed to test for intersections with a sphere in world space.
import math


class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def hits(self, sphere):
        # Tests for intersection with sphere in world space.
        # If no intersection occurs, return -1.
        # Else return multiplier t to reach closest hit point.
        # t is a multiplier as follows: self.origin + (self.direction * t).
        OC = sphere.center - self.origin
        Tca = OC.dot(self.direction)
        d = self.findOpposite(Tca, OC.magnitude)
        # If the point of closest approach is farther away from the center than
        # the radius is long, there is no hit.
        if(d > sphere.radius):
            return -1
        # Find the distance of the closest surface collision of ray and sphere:
        Thc = self.findOpposite(d, sphere.radius)
        return Tca - Thc

    def findOpposite(self, adj, hyp):
        # Use the pythagorean theorem to find the length
        # of the opposite side.
        return math.sqrt(math.pow(hyp, 2) - math.pow(adj, 2))

    def __repr__(self):
        return("Origin: " + str(self.origin) + " Direction: " + str(self.direction))
