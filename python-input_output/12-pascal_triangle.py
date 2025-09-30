#!/usr/bin/python3
"""
Module that provides a function to return the JSON representation
of an object (string).
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of size n.
    Each list inside the main list represents a row
    of Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(row)
        prev_row = row
    return triangle
