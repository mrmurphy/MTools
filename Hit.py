# A simple object representing a ray hit with a sphere.


class Hit(object):
    def __init__(self, dist, worldHit, normal, objColor):
        # Dist shoudl be a scalar, and normal shoudl be a vector object.
        self.dist =  dist
        self.worldHit = worldHit
        self.normal = normal
        self.objColor = objColor
