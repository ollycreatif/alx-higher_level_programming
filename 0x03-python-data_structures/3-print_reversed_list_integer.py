#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        # for x in reversed(my_list):
        #     print("{:d}".format(x))

        for x in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[x]))

        # x = len(my_list) - 1
        # while x >= 0:
        #     print("{:d}".format(my_list[x]))
        #     x -= 1
