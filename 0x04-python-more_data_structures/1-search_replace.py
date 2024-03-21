#!/usr/bin/python3
# replaces all occurrences of an element
# by another in a new list
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for x in range(len(new_list)):
        if new_list[x] == search:
            new_list[x] = replace
    return new_list
