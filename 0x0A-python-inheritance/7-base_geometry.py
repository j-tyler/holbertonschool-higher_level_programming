#!/usr/bin/python3
"""
Base class for Geometry
"""


class BaseGeometry:
    """
    Base class for Geometry
    """
    def area(self):
        """
        Base area function
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Defines valid input
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
