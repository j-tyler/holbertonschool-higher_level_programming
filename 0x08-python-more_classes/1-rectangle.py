#!/usr/bin/python3
"""
This is a class for a Rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
    def height(self):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
