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
