#!/usr/bin/python3
"""

Module contains one function that adds up 2 integers

"""


def add_integer(a, b=98):
    """Sums two integers or floats as integers

    Args:
        a: first argument
        b: second argument

    Returns:
        integer value of sum

    Raises:
        TypeError: if a or b is neither an integer nor a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
