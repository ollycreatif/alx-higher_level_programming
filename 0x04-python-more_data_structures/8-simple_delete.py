#!/usr/bin/python3

# deletes a key in a dictionary
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        a_dictionary
    else:
        del a_dictionary[key]
    return a_dictionary
