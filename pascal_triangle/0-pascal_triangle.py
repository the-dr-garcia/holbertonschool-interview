#!/usr/bin/env python3
"""Module to generate Pascal's triangle of n."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]
        for j in range(len(prev_row) - 1):
            current_row.append(prev_row[j] + prev_row[j + 1])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
