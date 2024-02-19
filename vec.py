from math import sin, cos, sqrt, acos

class Vec:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def new_spherical(r, polar, azimuth):
        return Vec(r*sin(polar)*cos(azimuth), r*sin(polar)*sin(azimuth), r*cos(polar))
    
    def dot(vec1, vec2):
        return (vec1.x*vec2.x + vec1.y*vec2.y + vec1.z*vec2.z)

    def cross(vec1, vec2):
        return Vec(vec1.y*vec2.z - vec1.z*vec2.y, vec1.z*vec2.x - vec1.x*vec2.z, vec1.x*vec2.y - vec1.y*vec2.x)

    def angle_between(vec1, vec2):
        return acos(Vec.dot(vec1, vec2)/(vec1.mag()*vec2.mag()))

    def mag_squared(self):
        return Vec.dot(self, self)
    
    def mag(self):
        return sqrt(self.mag_squared())

    def norm(self):
        return self / self.mag()

    def rotated(self, axis, angle):
        axis = axis.norm()
        return cos(angle)*self + sin(angle)*Vec.cross(axis, self) + (1 - cos(angle))*Vec.dot(axis, self)*axis

    def __mul__(self, scalar):
        return Vec(self.x*scalar, self.y*scalar, self.z*scalar)
    
    def __rmul__(self, scalar):
        return Vec(self.x*scalar, self.y*scalar, self.z*scalar)

    def __truediv__(self, scalar):
        return Vec(self.x/scalar, self.y/scalar, self.z/scalar)

    def __add__(self, vector):
        return Vec(self.x+vector.x, self.y+vector.y, self.z+vector.z)

    def __sub__(self, vector):
        return Vec(self.x-vector.x, self.y-vector.y, self.z-vector.z)

    def __neg__(self):
        return Vec(-self.x, -self.y, -self.z)

    def __abs__(self):
        return self.mag()