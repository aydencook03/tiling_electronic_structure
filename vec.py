from math import sin, cos, sqrt, acos, atan2

PRECISION = 10

##############################################################################################


class Vec:
    """
    A 2d vector object.

    This consolidates a lot of the math. By rounding values to PRECISION digits we are able to
    define __hash__ and __eq__, which allows us to prevent duplications due to floating point errors.

    This hashability carries forward to the other object types like shapes and particles that use Vec, allowing
    us to use sets to prevent duplications.
    """

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    @staticmethod
    def new_polar(r, angle):
        return Vec(r*cos(angle), r*sin(angle))

    @staticmethod
    def from_coords(coord_pair, basis_pair):
        return coord_pair[0]*basis_pair[0] + coord_pair[1]*basis_pair[1]

    @staticmethod
    def dot(vec1, vec2):
        return (vec1.x*vec2.x + vec1.y*vec2.y)

    @staticmethod
    def cross(vec1, vec2):
        return (vec1.x*vec2.y - vec1.y*vec2.x)

    @staticmethod
    def angle_between(vec1, vec2):
        return acos(Vec.dot(vec1, vec2)/(vec1.mag()*vec2.mag()))

    def mag_squared(self):
        return Vec.dot(self, self)

    def mag(self):
        return sqrt(self.mag_squared())

    def angle(self):
        return atan2(self.y, self.x)

    def norm(self):
        return self / self.mag()

    def rotated(self, angle):
        return Vec.new_polar(self.mag(), angle + self.angle())

    def __mul__(self, scalar):
        return Vec(self.x*scalar, self.y*scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return Vec(self.x/scalar, self.y/scalar)

    def __add__(self, vector):
        return Vec(self.x+vector.x, self.y+vector.y)

    def __sub__(self, vector):
        return Vec(self.x-vector.x, self.y-vector.y)

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def __abs__(self):
        return self.mag()

    def __eq__(self, other):
        x_close = round(self.x, PRECISION) == round(other.x, PRECISION)
        y_close = round(self.y, PRECISION) == round(other.y, PRECISION)
        return isinstance(other, Vec) and x_close and y_close

    def __hash__(self):
        return hash((round(self.x, PRECISION), round(self.y, PRECISION)))

##############################################################################################
