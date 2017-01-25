#!/usr/bin/python3
"""
This is a class for a Rectangle
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

    def __str__(self):
        string = "{}".format('\n'.join([Rectangle.print_symbol * self.__width
                 for row in range(0, self.__height)]))
        return string

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def print_symbol():
        return Rectangle.print_symbol

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
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height

    @print_symbol.setter
    def print_symbol(self, value):
        Rectangle.print_symbol = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
