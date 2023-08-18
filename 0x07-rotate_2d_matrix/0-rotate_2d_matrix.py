#!/usr/bin/python3
"""
This script perform the transpose of a matrix by rotating clockwise
"""


def rotate_2d_matrix(matrix):
    """ This function performs the transpose of matrix """
    size = len(matrix)
    layers = size // 2

    for layer in range(0, layers):
        first = layer
        last = size - first - 1

        for element in range(first, last):
            offset = element - first

            top_left = matrix[first][element]
            top_right = matrix[element][last]
            bottom_right = matrix[last][last-offset]
            bottom_left = matrix[last-offset][first]

            matrix[first][element] = bottom_left
            matrix[element][last] = top_left
            matrix[last][last-offset] = top_right
            matrix[last-offset][first] = bottom_right
