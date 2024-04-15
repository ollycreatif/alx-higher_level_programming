#!/usr/bin/python3
"""Inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intializing a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
