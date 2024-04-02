#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as err:
        stderr.write("Exception: " + str(err) + "\n")
        return False
    return True
