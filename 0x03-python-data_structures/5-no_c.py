#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ""
    for strx in my_string:
        if 'C' != strx != 'c':
            my_new_string += strx
    return my_new_string
