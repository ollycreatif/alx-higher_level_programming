#!/usr/bin/python3

# returns a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    new_dico = a_dictionary.copy()
    for k, v in new_dico.items():
        v *= 2
        new_dico[k] = v
    return new_dico
