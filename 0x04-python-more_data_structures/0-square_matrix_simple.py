#!/usr/bin/python3

#  computes the square value of all integers of a matrix
def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda x: x ** 2, y)) for y in matrix]
    return new_matrix
