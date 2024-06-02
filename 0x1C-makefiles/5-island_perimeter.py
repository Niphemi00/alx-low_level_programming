#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): The grid representing the map with 0s and 1s.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell contributes 4 to the perimeter
                perimeter += 4
                # If the cell above is also land, subtract 2 from perimeter
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                # If the cell to the left is also land, subtract 2 from perimeter
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter
