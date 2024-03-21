#!/usr/bin/python3

# computes the square value of all integers of a matrix using map()
def square_matrix_map(matrix=[]):
    new_matrix = list(map((lambda row: list(map((lambda x: x * x), row))), matrix))
    return new_matrix
