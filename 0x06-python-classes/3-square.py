#!/usr.bin/python3
''' Defines a class called Square
'''


class Square:
    ''' Represents class Square '''
    def __init__(self, size=0):
        '''Instance attribute initialization
        Args:
            size: size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        '''Area of Square
        Return: value of area
        '''
        return (self.__size ** 2)
