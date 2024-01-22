#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for row in matrix:
            print(' '.join(map(str, row)))
