#!/usr/bin/python3
"""
This script solves the Island perimeter graph problem
"""


def island_perimeter(grid):
    """ This function solves the island perimeter. """
    visit = set()

    def dfs(i, j):
        """ This function implements dfs algorithms. """
        if i >= len(grid) or j >= len(grid[0]) or \
           i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        if (i, j) in visit:
            return 0

        visit.add((i, j))
        perm = dfs(i, j + 1)
        perm += dfs(i + 1, j)
        perm += dfs(i, j - 1)
        perm += dfs(i - 1, j)
        return perm

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j)
