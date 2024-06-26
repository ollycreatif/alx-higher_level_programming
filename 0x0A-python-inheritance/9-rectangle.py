#!/usr/bin/python3
"""Defines a class Rectangle to inherit from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intializing a new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() representation of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
