#!/usr/bin/python3

# function that adds all unique integers in a list
# (only once for each integer)
def uniq_add(my_list=[]):
    u_sum = 0
    for x in set(my_list):
        u_sum += x
    return u_sum
