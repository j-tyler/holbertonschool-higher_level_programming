#!/usr/bin/python3
"""
This is a class for a Rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        string = "{}".format('\n'.join(['#' * self.__width for row in
                 range(0, self.__height)]))
        return string

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
