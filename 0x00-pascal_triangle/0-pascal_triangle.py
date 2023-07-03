#!/usr/bin/python3
"""
This is a python implimentation of Pascal triangle
"""


def pascal_triangle(n):
    """ This function produces the pascal triangle. """
    if n <= 0:
        return []
    else:
        res = [[1]]

        for i in range(n - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
