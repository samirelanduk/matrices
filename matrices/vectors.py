"""Contains the Vector class."""

class Vector:
    """A vector is a sequence of numbers. They can represent a point in space,
    or the attributes of an object.

    :param values: The numbers that make up the Vector. If a single sequence is
    given, that sequence will be unpacked to make the vector."""

    def __init__(self, *values):
        if len(values) == 1:
            try:
                self._values = list(values[0])
            except TypeError:
                self._values = list(values)
        else:
            self._values = list(values)


    def __repr__(self):
        return "<Vector {}>".format(self._values)


    def __len__(self):
        return len(self._values)


    def length(self):
        """Returns the length of the Vector.

        :rtype: ``int``"""

        return len(self)


    def dot(self, other):
        """Returns the dot product between this vector and another.

        :param Vector other: The other Vector.
        :raises TypeError: If a non-Vector is given.
        :rtype: ``float``"""

        if not isinstance(other, Vector):
            raise TypeError("{} is not a Vector".format(other))
        if self.length() != other.length():
            raise ValueError("{} and {} are not equal length".format(self, other))
        return sum([u_i * v_i for u_i, v_i in zip(self._values, other._values)])
