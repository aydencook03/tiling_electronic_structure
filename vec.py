from math import sin, cos, sqrt, acos, atan2, isclose

GRANULARITY = 1e-1  # define the granularity for rounding and comparison

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
        # Round the values to the nearest granularity step
        self.x = round(float(x) / GRANULARITY) * GRANULARITY
        self.y = round(float(y) / GRANULARITY) * GRANULARITY

    @staticmethod
    def new_polar(r, angle):
        return Vec(r*cos(angle), r*sin(angle))

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
        # Use the granularity to check if two Vecs are close enough to be considered equal
        return isinstance(other, Vec) and isclose(self.x, other.x, abs_tol=GRANULARITY) and isclose(self.y, other.y, abs_tol=GRANULARITY)

    def __hash__(self):
        return hash((self.x, self.y))


##############################################################################################
