#!/usr/bin/python3
"""Inherits a list class"""


class MyList(list):
    """Inherits a list class"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
