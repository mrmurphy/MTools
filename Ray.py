# A simple definition of an array.
# Designed to test for intersections with a sphere in world space.
from MTools.Hit import Hit
import math


class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

    def hits(self, sphere):
        # Tests for intersection with sphere in world space.
        # If no intersection occurs, returns None.
        # Else return multiplier t to reach closest hit point.
        # t is a multiplier as follows: self.origin + (self.direction * t).
        OC = sphere.center - self.origin
        Tca = OC.dot(self.direction)
        d = self.findOpposite(Tca, OC.magnitude)
        # If the point of closest approach is farther away from the center than
        # the radius is long, there is no hit.
        if(d > sphere.radius or d < 0):
            return None
        # Find the distance from the camera to the collision point:
        Thc = self.findOpposite(d, sphere.radius)
        T = Tca - Thc
        # Find the hit point in world space:
        worldHit = (self.direction * T) + self.origin
        #Construct the surface normal of the hit point.
        normal = ((worldHit - sphere.center).normalize())
        # Build the hit object to return.
        result = Hit(Tca - Thc, worldHit, normal, sphere.color)
        return result

    def findOpposite(self, adj, hyp):
        # Use the pythagorean theorem to find the length
        # of the opposite side.
        return math.sqrt(math.pow(hyp, 2) - math.pow(adj, 2))

    def __repr__(self):
        return("Origin: " + str(self.origin) + " Direction: " + str(self.direction))
