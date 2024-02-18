from math import sin, cos, sqrt

class Vec:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    @classmethod
    def new_spherical(cls, r, polar, azimuth):
        return cls(r*sin(polar)*cos(azimuth), r*sin(polar)*sin(azimuth), r*cos(polar))
    
    @staticmethod
    def dot(vec1, vec2):
        return (vec1.x*vec2.x + vec1.y*vec2.y + vec1.z*vec2.z)

    @staticmethod
    def cross(vec1, vec2):
        return Vec(vec1.y*vec2.z - vec1.z*vec2.y, vec1.z*vec2.x - vec1.x*vec2.z, vec1.x*vec2.y - vec1.y*vec2.x)

    def mag_squared(self):
        return dot(self, self)
    
    def mag(self):
        return sqrt(self.mag_squared())

    def norm(self):
        return self / self.mag()