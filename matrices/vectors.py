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
