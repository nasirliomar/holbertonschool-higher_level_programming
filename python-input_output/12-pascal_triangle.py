#!/usr/bin/python3
"""Module: pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last = triangle[-1]
            for j in range(1, len(last)):
                row.append(last[j - 1] + last[j])
            row.append(1)
        triangle.append(row)

    return triangle
